Issue Summary
On March 24, 2024, at 10:00 AM UTC, our Apache web server began returning a 500 Internal Server Error for users attempting to access the site. The outage lasted until 10:30 AM UTC, resulting in a 30-minute downtime. During this period, users experienced service unavailability, primarily those accessing the WordPress site hosted on the server. The root cause of the issue was identified as a misconfigured PHP file extension, where a file was incorrectly named with a phpp extension instead of php .php.
Timeline
10:00 AM: The issue was detected.
10:05 AM: An investigation was initiated, suspecting a potential misconfiguration or file permission issue.
10:10 AM: strace and tmux were used to attach to the Apache process and simulate a request using curl to gather more information about the error.
10:20 AM: The team identified that Apache was unable to access a required PHP file due to the incorrect file extension.
10:30 AM: The issue was resolved by renaming the file from .phpp to .php, and the Apache service was restarted.
Root Cause and Resolution
The root cause of the 500 Internal Server Error was a misconfigured PHP file extension. The file responsible for handling requests was incorrectly named with a .phpp extension, which Apache could not process as a valid PHP file. This misconfiguration prevented the server from executing the necessary PHP code, resulting in the 500 error.
To resolve the issue, the following steps were taken:
The file was renamed from script.phpp to script.php. Puppet manifest was created to automate the rename of the files with incorrect extensions
The Apache service was restarted to ensure that the changes took effect.
Corrective and Preventative Measures
To prevent similar issues in the future, the following improvements and tasks are recommended:
 Implement strict file naming conventions and validation checks.
Set up automated monitoring and alerting for 500 Internal Server Errors.
Create a Puppet manifest to automate the renaming of files with incorrect extensions and ensure that the Apache service is restarted as needed.
