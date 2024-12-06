# jenkins-cicd Python Jenkins CI/CD
# Jenkins CI/CD Pipeline Project

This project automates the CI/CD process for deploying and managing a Python-based application using Jenkins. The pipeline integrates version control, environment setup, dependency installation, code quality checks, and test execution to streamline the development workflow.

## Project Structure

### Repository Overview
The repository is hosted on GitHub at: [https://github.com/favy12/jenkins-cicd.git](https://github.com/favy12/jenkins-cicd.git).

### Key Files
- **Jenkinsfile**: Defines the CI/CD pipeline stages and steps.
- **Application Code**: Python source code located in the repository.
- **Requirements File**: Specifies Python dependencies.

## Pipeline Stages

1. **Checkout SCM**
   - Retrieves the source code from the GitHub repository.

2. **Setup Environment**
   - Cleans the workspace.
   - Clones the repository.
   - Sets up a Python virtual environment using `venv`.

3. **Install Dependencies**
   - Installs required Python libraries from `requirements.txt`.

4. **Linting**
   - Performs code quality checks using `pylint` or a similar tool.

5. **Run Tests**
   - Executes unit tests to validate functionality.

6. **Publish Test Results**
   - Aggregates and reports test results.

7. **Cleanup**
   - Cleans up temporary files and workspace to ensure a clean state for the next build.

## Prerequisites

1. **Jenkins Setup**
   - Jenkins installed and configured.
   - Required plugins:
     - Git Plugin
     - Pipeline Plugin
     - Python Plugin (if applicable)

2. **AWS EC2 Instance**
   - Jenkins server running on an EC2 instance.
   - Properly configured security groups to allow access.

3. **Python Environment**
   - Python 3.x installed.
   - Virtual environment (`venv`) setup.

4. **Network and IAM Configuration**
   - Ensure appropriate IAM roles and network settings for Jenkins to interact with the EC2 instance and GitHub.

## Troubleshooting

### Common Issues

- **Git Tool Not Configured**:
  Ensure the correct Git tool is installed and configured in Jenkins.
  
- **Python Virtual Environment Errors**:
  Confirm that the `venv` module is available. Use `python3 -m venv` to initialize the environment.
  
- **Instance Connection Failure**:
  Check EC2 security group rules, network configurations, and AWS documentation: [EC2 Instance Connect Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.html).

- **1/2 Status Checks Passed**:
  Review system logs and AWS instance health. Reboot or troubleshoot using AWS recommendations.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/favy12/jenkins-cicd.git
   ```

2. Set up the Jenkins job:
   - Select "Pipeline" as the job type.
   - Configure the job to fetch the Jenkinsfile from the repository.

3. Run the pipeline:
   - Monitor the stages and logs in the Jenkins console.

4. Debug issues:
   - Refer to the logs for specific error messages.
   - Use AWS tools for additional insights into EC2 instance issues.

## Future Improvements

- Add Docker support for consistent environment management.
- Implement additional testing stages (e.g., integration tests).
- Automate deployment to staging or production environments.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

For more information or to contribute, contact [favy12](https://github.com/favy12).


