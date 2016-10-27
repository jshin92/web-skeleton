import argparse
import os

def emit_html(project_name):
    with open(os.path.join(project_name, project_name + '.html'), 'w') as html_file:
        html_file.write('<html>\n')
        html_file.write('  <head>\n')
        html_file.write('    <title>TITLE</title>\n')
        html_file.write('    <meta charset="utf-8">\n')
        html_file.write('  </head>\n')
        html_file.write('  <body>\n')
        html_file.write('  </body>\n')
        html_file.write('</html>\n')

def main():
    parser = argparse.ArgumentParser(description='Creates a folder for a new web project, along with a skeleton html file')
    parser.add_argument('-p', '--project-name', help='Name of the project', required=True)
    args = parser.parse_args()
    if not os.path.exists(args.project_name):
        os.makedirs(args.project_name)
    emit_html(args.project_name)


if __name__ == '__main__':
    main()
