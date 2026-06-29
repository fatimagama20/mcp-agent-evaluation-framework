class HTMLReport:

    def generate(self, report):

        html = f"""
        <!DOCTYPE html>

        <html>

        <head>

            <title>AI Evaluation Report</title>

            <style>

                body {{
                    font-family: Arial;
                    margin:40px;
                    background:#f4f4f4;
                }}

                h1 {{
                    color:#1f4e79;
                }}

                table {{

                    border-collapse: collapse;

                    width:100%;

                    background:white;

                }}

                th, td {{

                    border:1px solid #ddd;

                    padding:10px;

                    text-align:left;

                }}

                th {{

                    background:#1f4e79;

                    color:white;

                }}

                .card {{

                    background:white;

                    padding:20px;

                    margin-bottom:20px;

                    border-radius:8px;

                }}

            </style>

        </head>

        <body>

        <h1>AI Evaluation Dashboard</h1>

        <div class="card">

            <h3>Summary</h3>

            <p><b>Accuracy:</b> {report["accuracy"]:.2f}%</p>

            <p><b>Hallucination Rate:</b> {report["hallucination_rate"]:.2f}%</p>

            <p><b>Average Relevancy:</b> {report["average_relevancy"]:.2f}</p>

            <p><b>Average Latency:</b> {report["average_latency"]:.2f} sec</p>

        </div>

        <table>

        <tr>

            <th>Question</th>

            <th>Expected</th>

            <th>Answer</th>

            <th>Passed</th>

            <th>Relevancy</th>

            <th>Latency</th>

        </tr>
        """
        for result in report["results"]:
            row_color = "#e8f5e9" if result["passed"] else "#ffebee"

            html += f"""

            <tr style="background:{row_color};">

                <td>{result["question"]}</td>

                <td>{result["expected_answer"]}</td>

                <td>{result["answer"]}</td>

                <td>{"🟢 PASS" if result["passed"] else "🔴 FAIL"}</td>

                <td>{result["relevancy"]:.2f}</td>

                <td>{result["latency"]:.2f}</td>

            </tr>

            """
        html += """

        </table>

        </body>

        </html>

        """

        with open(

            "reports/evaluation_report.html",

            "w",

            encoding="utf-8"

        ) as f:

            f.write(html)