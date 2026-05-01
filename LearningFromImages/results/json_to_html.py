import json
from pathlib import Path
from html import escape
import markdown

def json_to_html2(json_path, output_html="output.html"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    html_parts = []
    html_parts.append("""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Benchmark Conversations</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                padding: 20px;
            }
            .conversation {
                margin-bottom: 40px;
                padding: 15px;
                background: white;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            .turn {
                margin-bottom: 15px;
            }
            .user {
                background-color: #e3f2fd;
                padding: 10px;
                border-radius: 8px;
                margin-right: 20%;
            }
            .assistant {
                background-color: #e8f5e9;
                padding: 10px;
                border-radius: 8px;
                margin-left: 20%;
            }
            .meta {
                font-size: 12px;
                color: #666;
                margin-bottom: 5px;
            }
            .raw {
                display: none;
                background: #fafafa;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ddd;
                margin-top: 5px;
                word-break: break-all;
            }
            button {
                margin-top: 5px;
                font-size: 12px;
            }
            .inline-image {
                max-width: 300px;
                max-height: 300px;
                border-radius: 6px;
                border: 1px solid #ccc;
                margin-top: 6px;
                display: block;
            }
            pre {
                white-space: pre-wrap;
            }
        </style>
        <script>
            function toggleRaw(id, btn) {
                var el = document.getElementById(id);
                var current = window.getComputedStyle(el).display;
                if (current === "none") {
                    el.style.display = "block";
                    btn.textContent = "Hide Raw";
                } else {
                    el.style.display = "none";
                    btn.textContent = "Show Raw";
                }
            }
        </script>
    </head>
    <body>
    <h1>Benchmark Conversations</h1>
    """)

    counter = 0

    for i, conv in enumerate(data.get("conversations", [])):
        if i == 0:
            html_parts.append('<div class="conversation">')
            html_parts.append(f"<h2>Task ID: {escape(str(conv.get('id', '')))}</h2>")
            continue

        html_parts.append('<div class="conversation">')
        html_parts.append(f"<h2>Conversation ID: {escape(str(conv.get('id', '')))}</h2>")

        for req in conv.get("requests", []):
            for content in req.get("contents", []):
                role = content.get("role", "")
                parts = content.get("parts", [])

                label = "User" if role == "CONTENT_ROLE_USER" else "Assistant"
                css_class = "user" if role == "CONTENT_ROLE_USER" else "assistant"

                for part in parts:
                    raw_id = f"raw_{counter}"
                    counter += 1

                    inline_data = part.get("inlineData")
                    if inline_data:
                        mime_type = inline_data.get("mimeType", "image/jpeg")
                        b64_data = inline_data.get("data", "")
                        truncated = b64_data[:80] + "..." if len(b64_data) > 80 else b64_data
                        html_parts.append(f"""
                        <div class="turn {css_class}">
                            <div class="meta"><strong>{label}</strong> <em>[image]</em></div>
                            <img class="inline-image"
                                 src="data:{mime_type};base64,{b64_data}"
                                 alt="Inline image" />
                            <button onclick="toggleRaw('{raw_id}', this)">Show Raw</button>
                            <div id="{raw_id}" class="raw">
                                <pre>mimeType: {escape(mime_type)}\ndata: {escape(truncated)}</pre>
                            </div>
                        </div>
                        """)
                        continue

                    raw_text = part.get("text", "")
                    if not raw_text:
                        continue

                    # Try to decode nested JSON string for assistant responses
                    rendered_html = None
                    pretty_json = None
                    decoded_success = False

                    if role == "CONTENT_ROLE_ASSISTANT":
                        s = raw_text.strip()
                        # Often wrapped in quotes in the file (starts and ends with ")
                        if s.startswith('"') and s.endswith('"'):
                            # First unescape the outer JSON string
                            try:
                                s = json.loads(s)
                            except Exception:
                                pass  # leave as-is if it fails

                        # Now, see if s itself is JSON (object/array)
                        try:
                            maybe_obj = json.loads(s)
                            # If it's a JSON object or list, pretty-print it
                            if isinstance(maybe_obj, (dict, list)):
                                pretty_json = json.dumps(maybe_obj, indent=2, ensure_ascii=False)
                                decoded_success = True
                        except Exception:
                            decoded_success = False

                    if decoded_success and pretty_json is not None:
                        # Show the pretty JSON in rendered view
                        escaped_render = escape(pretty_json)
                        html_parts.append(f"""
                        <div class="turn {css_class}">
                            <div class="meta"><strong>{label}</strong> <em>[decoded JSON]</em></div>
                            <pre class="rendered">{escaped_render}</pre>
                            <button onclick="toggleRaw('{raw_id}', this)">Show Raw</button>
                            <div id="{raw_id}" class="raw">
                                <pre>{escape(raw_text)}</pre>
                            </div>
                        </div>
                        """)
                    else:
                        # Fallback: normal markdown rendering
                        escaped_text = escape(raw_text)
                        rendered_html = markdown.markdown(raw_text)

                        html_parts.append(f"""
                        <div class="turn {css_class}">
                            <div class="meta"><strong>{label}</strong></div>
                            <div class="rendered">{rendered_html}</div>
                            <button onclick="toggleRaw('{raw_id}', this)">Show Raw</button>
                            <div id="{raw_id}" class="raw">
                                <pre>{escaped_text}</pre>
                            </div>
                        </div>
                        """)

        html_parts.append("</div>")

    html_parts.append("</body></html>")

    with open(output_html, "w", encoding="utf-8") as f:
        f.write("\n".join(html_parts))

    print(f"HTML file saved to: {output_html}")


# def json_to_html2(json_path, output_html="output.html"):
#     with open(json_path, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     html_parts = []
#     html_parts.append("""
#     <html>
#     <head>
#         <meta charset="UTF-8">
#         <title>Benchmark Conversations</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 background-color: #f5f5f5;
#                 padding: 20px;
#             }
#             .conversation {
#                 margin-bottom: 40px;
#                 padding: 15px;
#                 background: white;
#                 border-radius: 10px;
#                 box-shadow: 0 2px 5px rgba(0,0,0,0.1);
#             }
#             .turn {
#                 margin-bottom: 15px;
#             }
#             .user {
#                 background-color: #e3f2fd;
#                 padding: 10px;
#                 border-radius: 8px;
#                 margin-right: 20%;
#             }
#             .assistant {
#                 background-color: #e8f5e9;
#                 padding: 10px;
#                 border-radius: 8px;
#                 margin-left: 20%;
#             }
#             .meta {
#                 font-size: 12px;
#                 color: #666;
#                 margin-bottom: 5px;
#             }
#             .raw {
#                 display: none;
#                 background: #fafafa;
#                 padding: 10px;
#                 border-radius: 5px;
#                 border: 1px solid #ddd;
#                 margin-top: 5px;
#                 word-break: break-all;
#             }
#             button {
#                 margin-top: 5px;
#                 font-size: 12px;
#             }
#             .inline-image {
#                 max-width: 300px;
#                 max-height: 300px;
#                 border-radius: 6px;
#                 border: 1px solid #ccc;
#                 margin-top: 6px;
#                 display: block;
#             }
#         </style>
#         <script>
#             function toggleRaw(id, btn) {
#                 var el = document.getElementById(id);
#                 var current = window.getComputedStyle(el).display;
#                 if (current === "none") {
#                     el.style.display = "block";
#                     btn.textContent = "Hide Raw";
#                 } else {
#                     el.style.display = "none";
#                     btn.textContent = "Show Raw";
#                 }
#             }
#         </script>
#     </head>
#     <body>
#     <h1>Benchmark Conversations</h1>
#     """)

#     counter = 0

#     for i,conv in enumerate(data.get("conversations", [])):
#         if i == 0:
#             html_parts.append('<div class="conversation">')
#             html_parts.append(f"<h2>Task ID: {escape(str(conv.get('id', '')))}</h2>")
#             continue

#         html_parts.append('<div class="conversation">')
#         html_parts.append(f"<h2>Conversation ID: {escape(str(conv.get('id', '')))}</h2>")

#         for req in conv.get("requests", []):
#             for content in req.get("contents", []):
#                 role = content.get("role", "")
#                 parts = content.get("parts", [])

#                 label = "User" if role == "CONTENT_ROLE_USER" else "Assistant"
#                 css_class = "user" if role == "CONTENT_ROLE_USER" else "assistant"

#                 for part in parts:
#                     raw_id = f"raw_{counter}"
#                     counter += 1

#                     # Check for inline image data
#                     inline_data = part.get("inlineData")
#                     if inline_data:
#                         mime_type = inline_data.get("mimeType", "image/jpeg")
#                         b64_data = inline_data.get("data", "")
#                         # Show only first 80 chars of base64 in raw view
#                         truncated = b64_data[:80] + "..." if len(b64_data) > 80 else b64_data
#                         html_parts.append(f"""
#                         <div class="turn {css_class}">
#                             <div class="meta"><strong>{label}</strong> <em>[image]</em></div>
#                             <img class="inline-image"
#                                  src="data:{mime_type};base64,{b64_data}"
#                                  alt="Inline image" />
#                             <button onclick="toggleRaw('{raw_id}', this)">Show Raw</button>
#                             <div id="{raw_id}" class="raw">
#                                 <pre>mimeType: {escape(mime_type)}\ndata: {escape(truncated)}</pre>
#                             </div>
#                         </div>
#                         """)
#                         continue

#                     # Text part
#                     raw_text = part.get("text", "")
#                     if not raw_text:
#                         continue

#                     escaped_text = escape(raw_text)
#                     rendered_html = markdown.markdown(raw_text)

#                     html_parts.append(f"""
#                     <div class="turn {css_class}">
#                         <div class="meta"><strong>{label}</strong></div>
#                         <div class="rendered">{rendered_html}</div>
#                         <button onclick="toggleRaw('{raw_id}', this)">Show Raw</button>
#                         <div id="{raw_id}" class="raw">
#                             <pre>{escaped_text}</pre>
#                         </div>
#                     </div>
#                     """)

#         html_parts.append("</div>")

#     html_parts.append("</body></html>")

#     with open(output_html, "w", encoding="utf-8") as f:
#         f.write("\n".join(html_parts))

#     print(f"HTML file saved to: {output_html}")



def convert_all_json_in_dir(input_dir, output_dir=None):
    input_dir = Path(input_dir)

    # If no output_dir specified, use same directory
    if output_dir is None:
        output_dir = input_dir
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    json_files = list(input_dir.rglob("*.json"))  # recursive search

    if not json_files:
        print("No JSON files found.")
        return

    for json_file in json_files:
        try:
            # Create output path
            relative_path = json_file.relative_to(input_dir)
            output_path = (output_dir / relative_path).with_suffix(".html")

            # Ensure subdirectories exist
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Convert
            json_to_html2(json_file, output_path)

            print(f"Converted: {json_file} → {output_path}")

        except Exception as e:
            print(f"Failed: {json_file} | Error: {e}")


# Example usage
convert_all_json_in_dir('raw_json/Anthropic', 'html/Anthropic')