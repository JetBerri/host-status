import os
import re

def mjml():

    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    directory = "/opt/host-status/scripts/log/"

    files = os.listdir(directory)

    with open("/opt/host-status/scripts/index.mjml", "w") as f:
        f.write(f"""
<mjml>
    <mj-head>
        <mj-style>
            .space-background {{
                background-color: #0B0E1B;
                background-image: url("https://i.imgur.com/T1vDxhH.png");
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
            }}
            .content {{
                background-color: #1C1F3D;
                border-radius: 4px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
                margin: 50px auto;
                max-width: 600px;
                padding: 30px;
                text-align: center;
            }}
            .content h1 {{
                color: #fff;
                font-family: 'Montserrat', sans-serif;
                font-size: 40px;
                font-weight: 900;
                margin-bottom: 20px;
            }}
            .content p {{
                color: #fff;
                font-family: 'Montserrat', sans-serif;
                font-size: 18px;
                line-height: 1.6;
            }}
            .file-link {{
                background-color: #fff;
                border-radius: 4px;
                color: #1C1F3D;
                display: inline-block;
                font-family: 'Montserrat', sans-serif;
                font-size: 16px;
                margin: 20px auto;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                transition: background-color 0.3s;
            }}
            .file-link:hover {{
                background-color: #2E335F;
                color: #fff;
            }}
        </mj-style>
    </mj-head>
    <mj-body>
        <mj-container class="space-background">
            <mj-section>
                <mj-column>
                        <mj-text>
                            <h1>Attached files</h1>
                            <p>Here are the scanned IP addresses.</p>
                        </mj-text>
        """)

        for filename in files:
            if ip_pattern.match(filename):
                if filename.endswith(".yaml"):
                    yaml_file = os.path.join(directory, filename)
                    with open(yaml_file, 'r') as f_yaml:
                        yaml_content = f_yaml.read()

                    f.write(f"""
                        <mj-text>
                            <a class="file-link" href="http://localhost/{yaml_file}" download>Archivo YAML</a>
                        </mj-text>
                            """)
                elif filename.endswith(".txt"):
                    txt_file = os.path.join(directory, filename)
                    with open(txt_file, 'r') as f_txt:
                        txt_content = f_txt.read()

                    f.write(f"""
                        <mj-text>
                            <a class="file-link" href="http://localhost/{txt_file}" download>Archivo TXT</a>
                        </mj-text>
                            """)

        f.write(f"""
                    </mj-div>
                </mj-column>
            </mj-section>
        </mj-container>
    </mj-body>
</mjml>
        """)