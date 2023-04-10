import re

def generate_html_output(code, token_list):
    css_styles = '''
        <style>
            body { font-family: Helvetica; background-color: #121212; color: #ffffff; }
            .code-container { margin: 0 auto; width: 80%; }
            .h1-title { text-align: center; }
            .code-tag { font-size: 20px; white-space: pre-wrap; }
            .identifier { color: #de6b74; }
            .keyword { color: #c678dd; }
            .operator { color: #e5c07b; }
            .delimiter { color: #a4abb8; }
            .literal { color: #98c379; }
            .comment { color: #5c6370; font-style: italic; }
            .special-symbol { color: #e06c75; }
            .dashboardContainer { margin: 0 auto; width: 80%; }
            table { border-collapse: collapse; margin-top: 10px; }
            th, td { border: 1px solid #ffffff; padding: 5px; }
            th { background-color: #383838; }
            td:first-child { font-weight: bold; }
        </style>
    '''
    html_body = f'''
        <h1 class="h1-title">Syntax Higlighter</h1>
        <div class="code-container">
            <code class="code-tag">{code}</code>
        </div>
        <div class="dashboardContainer">
            <div class="dashboardBottom">
                <table>
                    <thead>
                        <tr>
                            <th>Value</th>
                            <th>Token</th>
                        </tr>
                    </thead>
                    <tbody>
    '''
    for i, (value, token) in enumerate(token_list):
        html_body += f'<tr key="{i}"><td>{value}</td><td>{token}</td></tr>'
    html_body += '''
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    '''

    html_output = f'<html><head>{css_styles}</head><body>{html_body}'
    return html_output
