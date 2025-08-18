# import logging
# import requests
# import json

# def check_and_send_email(monthly, daily, monthly_threshold_limit, daily_threshold_limit, email_enabled, email_sender_address, email_recipient_address):
#     subject_message = "Threshold Alert Details"
#     monthly_basis_alerts = []
#     day_basis_alert = []

#     # Check monthly data
#     for key, value in monthly.items():
#         if value > int(monthly_threshold_limit):
#             monthly_basis_alerts.append(f"Month: {key} | Count: {value} | Threshold: {monthly_threshold_limit}")

#     # Check daily data
#     for key, value in daily.items():
#         if value > int(daily_threshold_limit):
#             day_basis_alert.append(f"Day: {key} | Count: {value} | Threshold: {daily_threshold_limit}")

#     # Prepare email body
#     monthly_heading = "Monthly data Exceeding Threshold\n"
#     daily_heading = "Daily data Exceeding the Threshold\n"
#     monthly_body = "\n".join(monthly_basis_alerts) if monthly_basis_alerts else "No Monthly Data Exceeding the Threshold"
#     day_body = "\n".join(day_basis_alert) if day_basis_alert else "No Daily Data Exceeding the Threshold"
    
#     email_body = daily_heading + day_body + "\n\n" + monthly_heading + monthly_body

#     # Send email if alerts exist
#     if monthly_basis_alerts or day_basis_alert:
#         send_email(subject_message, email_body, email_enabled, email_sender_address, email_recipient_address)

# def send_email(subject, body, email_enabled, sender_address, recipient_address):
#     if not email_enabled:
#         logging.warning("Email notifications are disabled.")
#         return False

#     formatted_data = body
#     data = {
#         "Type": "EmailData",
#         "From": sender_address,
#         "To": recipient_address,
#         "Subject": subject,
#         "Body": formatted_data,
#         "CC": ""
#     }

#     try:
#         resp = requests.post("YOUR_EMAIL_API_URL", data=json.dumps(data), headers={"Content-Type": "application/json"})
#         if resp.status_code != 200:
#             logging.warning("Failed to send email notification [%s]. Status Code: %s, Response: %s", subject, resp.status_code, resp.text)
#             return False
        
#         logging.info("Email notification [%s] sent successfully.", subject)
#         return True

#     except Exception as err:
#         logging.error('send_email: Unexpected exception occurred - %s', err, exc_info=True)
#         return False




def send_email(report_date, i_message, monthly_basis_alerts, day_basis_alert):
    try:
        if not email_enabled:
            logging.warning("Email notifications are disabled.")
            return False

        monthly_body = '\n'.join(monthly_basis_alerts) if monthly_basis_alerts else "\nNo monthly data\n"
        day_body = '\n'.join(day_basis_alert) if day_basis_alert else "\nNo Day data\n"
        formatted_date = report_date.strftime("%Y-%m-%d")
        i_subject = f"eida-report - HDFS File Counts - {formatted_date}"

        # Create HTML email body
        data_body = f"""
        <html>
        <head>   
            <style>
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h2>HDFS File Counts Report</h2>
            <p>Date: <strong>{formatted_date}</strong></p>
            <table>
                <tr>
                    <th>Type</th>
                    <th>Data</th>
                </tr>
                <tr>
                    <td>Day Threshold Data</td>
                    <td>{day_body}</td>
                </tr>
                <tr>
                    <td>Monthly Threshold Exceeded Data</td>
                    <td>{monthly_body}</td>
                </tr>
            </table>
            <p>If you have any questions, please feel free to reach out.</p>
        </body>
        </html>
        """

        data = {
            "Type": "EmailData",
            "From": emailSenderAddress,
            "To": emailRecipientAddress,
            "Subject": i_subject,
            "Body": data_body,
            "CC": "BCC": ""
        }

        resp = requests.post(emailApiUrl, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        if resp.status_code != 200:
            logging.warning("Failed to send email notification [%s]. Status Code: %s, Response: %s", i_subject, resp.status_code, resp.text)
            return False

        logging.info("Email notification [%s] sent successfully.", i_subject)
        return True

    except Exception as err:
        logging.error("send_email: Unexpected exception occurred: %s", err, exc_info=True)



