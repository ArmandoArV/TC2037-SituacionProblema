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
    # Match the indentation spaces in the code
    indentation_spaces = re.match('^(\s+)', code)
    if indentation_spaces:
        indentation_spaces = indentation_spaces.group(1)
    else:
        indentation_spaces = ''

    # Indentation of each code line will be removed and replaced with a <span> tag
    # with class 'indentation'
    code_lines = code.split('\n')
    code_block = ''
    for line in code_lines:
        # Remove the indentation spaces and replace it with a <span> tag with class 'indentation'
        line = line.replace(indentation_spaces, f'<span class="indentation">{indentation_spaces}</span>')

        # Append the line to the code block
        code_block += f'{line}\n'

    html_body = f'''
        <h1 class="h1-title">Syntax Higlighter</h1>
        <div class="code-container">
            <code class="code-tag">{code_block}</code>
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
