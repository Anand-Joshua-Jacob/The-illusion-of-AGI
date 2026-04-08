import json
from pathlib import Path
from html import escape
import markdown


def json_to_html(json_path, output_html="output.html"):
    # Load JSON
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
            }
            button {
                margin-top: 5px;
                font-size: 12px;
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

    # Iterate conversations
    for conv in data.get("conversations", []):
        html_parts.append('<div class="conversation">')
        html_parts.append(f"<h2>Conversation ID: {conv.get('id')}</h2>")

        for req in conv.get("requests", []):
            for content in req.get("contents", []):
                role = content.get("role", "")
                parts = content.get("parts", [])

                for part in parts:
                    raw_text = part.get("text", "")
                    escaped_text = escape(raw_text)

                    # Convert Markdown → HTML
                    rendered_html = markdown.markdown(raw_text)

                    raw_id = f"raw_{counter}"
                    counter += 1

                    if role == "CONTENT_ROLE_USER":
                        label = "User"
                        css_class = "user"
                    else:
                        label = "Assistant"
                        css_class = "assistant"

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

    # Write output
    with open(output_html, "w", encoding="utf-8") as f:
        f.write("\n".join(html_parts))

    print(f"HTML file saved to: {output_html}")


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
            json_to_html(json_file, output_path)

            print(f"Converted: {json_file} → {output_path}")

        except Exception as e:
            print(f"Failed: {json_file} | Error: {e}")


# Example usage
convert_all_json_in_dir('json_chat_traces/google', 'html_chat_traces/google')