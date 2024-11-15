## CUSTOM EMAIL SENDER DASHBOARD USING STRAMLIT, OPENAI AND MAILGUN 

## PROJECT OVERVIEW 

The Custom Email Sender Dashboard is an innovative, user-friendly tool designed to revolutionize email campaigns. Built with Streamlit, it provides a seamless interface for sending personalized bulk emails efficiently, while leveraging the power of OpenAI's GPT for AI-driven content creation and Mailgun's API for reliable delivery and tracking.

This application is a one-stop solution for businesses, marketers, and individuals who need an intuitive yet powerful tool to manage email campaigns. Whether it's customizing email content with placeholders, scheduling emails for future delivery, or analyzing real-time delivery performance, the dashboard makes complex tasks simple and accessible to all.

## Why Choose This Application?
1. Personalization Made Simple: Upload CSV files with recipient details and use placeholders like {Name} or {Location} to dynamically create unique email content for each recipient.
2. AI-Powered Content Creation: Generate professional, engaging email templates in seconds using OpenAI's GPT technology.
3. Full Control of Campaigns: Schedule emails, control sending rates with throttling, and monitor email delivery in real time—all from a sleek dashboard.
4. Scalable and Reliable: Integrates seamlessly with Mailgun for high-performance email delivery, ensuring your emails reach the intended inboxes.

   
## Who Is It For?
This project caters to anyone who needs to send emails efficiently and at scale, including:

1. Small Businesses: Build strong customer relationships with personalized campaigns.
Marketers: Create engaging newsletters and promotional emails with ease.
2. Event Organizers: Send invitations or reminders to hundreds of participants in a few clicks.
3. Freelancers: Stay in touch with clients and prospects using professional, AI-driven emails.

## What Makes It Unique?
Unlike traditional email-sending tools, the Custom Email Sender Dashboard combines cutting-edge AI capabilities with practical campaign management features to deliver an unparalleled user experience. Whether you're looking to craft the perfect message or analyze campaign performance, this application empowers you to focus on what matters most—connecting with your audience.

## FEATURES 

1. CSV Upload: Upload recipient data via CSV files containing fields like email addresses, names, and other dynamic placeholders.Automatically validate CSV structure to ensure compliance (e.g., presence of Email column).
2. Template Personalization: Design customizable email templates with placeholders such as {Name} and {Location}.Dynamically fill placeholders using uploaded recipient data.
3. AI-Powered Content: Leverage OpenAI GPT for generating professional and tailored email content.Option to customize AI-generated text for greater flexibility.
4. Email Scheduling: Schedule emails for future delivery at specific times and dates.Use the built-in task scheduler to manage multiple campaigns seamlessly.
5. Throttling: Configure the sending rate (e.g., 10 emails/hour) to comply with API/ESP limits and avoid triggering rate caps.
6. Real-Time Analytics: Monitor email statuses live:
Sent: Successfully delivered emails.
Pending: Emails queued or scheduled for delivery.
Failed: Emails that encountered errors during sending.
Display a detailed log of email activity and error handling.
7. Log Management:Track every email sent with timestamped logs, recipient details, and delivery status.
Filter logs to analyze failed or pending emails.
8. Mailgun API Integration: Seamlessly send emails through the secure and reliable Mailgun ESP.
Benefit from Mailgun's tracking features for delivery reports.


## TECHNICAL REQUIREMENTS 

1. Python Version: 3.8 or higher.
2. libraries :
   1. streamlit -  Dashboard framework.
   2. pandas - Data manipulation and CSV processing.
   3. requests - API communication.
   4. openai - OpenAI API integration.
   5. apscheduler -  Scheduling emails.
   6. smtplib
   7. python-dotenv - Secure management of environment variables.
3. APIs:
    1. OpenAI GPT API for content generation.
    2. Mailgun API for email sending.

## SETUP AND INSTALLATION 

1. Clone the repository

```bash
git clone https://github.com/your-username/email-sender-dashboard.git
cd email-sender-dashboard
```

2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```bash

pip install -r requirements.txt

```

4.  Configure Environment Variables
Create a .env file in the root directory with the following keys:
```bash

OPENAI_API_KEY=your-openai-api-key
MAILGUN_API_KEY=your-mailgun-api-key
MAILGUN_DOMAIN=your-mailgun-domain

```

5.  Run the Application
Launch the Streamlit application:
```bash
streamlit run app.py

```

## USAGE INSTRUCTIONS

## Step 1: Upload Recipient Data

Upload a CSV file containing recipient details such as email addresses and placeholders. Ensure the file includes a column for Email and any additional fields used in your template.

Example CSV:

Email	Name	Location
john@example.com	John Doe	New York
jane@example.com	Jane Smith	San Francisco

## Step 2: Define an Email Template
Create an email template using placeholders (e.g., {Name}, {Location}):

```bash
Subject: Exclusive Offer for {Name}

Hi {Name},

We noticed you're from {Location}. Check out our latest offers tailored just for you!

Best regards,  
[Your Company Name]


```
## Step 3: Generate and Preview Emails
1. Automatically populate placeholders with data from the uploaded CSV.
2. Preview emails in the dashboard.

## Step 4: Choose Sending Options

1. Send Immediately: Click Send Emails to deliver emails right away.
2. Schedule: Select a date and time for future delivery.
3. Throttle: Set a limit for the number of emails sent per hour.

## Step 5: Monitor Email Delivery

View email statuses directly on the dashboard:

1. Sent: Successfully delivered emails.
2. Pending: Scheduled or queued emails.
3. Failed: Errors in delivery.

## Key Functionalities
## Dynamic Content Personalization
Automatically populate placeholders for personalized email content.
## AI-Powered Email Writing
Use OpenAI's GPT API to generate professional, engaging email content tailored to your needs.
## Scheduling and Throttling
Plan email campaigns and control sending rates to meet API/ESP limits.
## Real-Time Analytics
Monitor delivery, track errors, and review logs in the dashboard

## Error Handling
 
1. API Limits: Gracefully handles errors like rate limits or invalid requests.
2. CSV Validation: Ensures required columns (e.g., Email) exist.
3. Delivery Failures: Provides detailed error messages for undelivered emails.

## Known Issues and Limitations
1. API Usage: Heavy use may exhaust OpenAI and Mailgun free-tier quotas.
2. In-Memory Data: Logs and schedules reset when the app restarts.
3. Mailgun Free Tier: Limited monthly email quota.

## Future Enhancements
The Custom Email Sender Dashboard has immense potential for growth and scalability. Below are the proposed enhancements that can make the application more robust, user-friendly, and feature-rich.
1. Advanced Analytics:
Include open/click rates and campaign insights.
2. Database Integration:
Persist email logs and settings using SQLite/PostgreSQL.
3. Multi-ESP Support:
Add integrations with SendGrid, Amazon SES, etc.
4. User Authentication:
Implement login and role-based permissions.
5. Enhanced UI:
Provide a drag-and-drop or WYSIWYG email editor.
6. Email Templates Library:
Offer pre-designed templates for various use cases.

