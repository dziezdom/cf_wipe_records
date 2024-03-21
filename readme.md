## Cloudflare Bulk DNS Records Deletion Guide

This guide provides step-by-step instructions for preparing to use a Python script to bulk delete DNS records on Cloudflare. We'll cover how to find your API token and Zone ID, set up a custom API token with the correct permissions, and install the necessary Python library.

### Table of Contents

1. [Prerequisites](#prerequisites)
2. [Finding Your Cloudflare API Token](#finding-your-cloudflare-api-token)
3. [Creating a Custom API Token](#creating-a-custom-api-token)
4. [Finding Your Zone ID](#finding-your-zone-id)
5. [Installing the Requests Library](#installing-the-requests-library)
6. [Running the Script](#running-the-script)

### Prerequisites

- A Cloudflare account with access to the domain(s) you wish to manage.
- Python installed on your machine.
- Basic familiarity with using the command line or terminal.

### Finding Your Cloudflare API Token

To interact with Cloudflare's API, you'll need an API token. Cloudflare provides a way to generate tokens with specific permissions tailored to your needs.

### Creating a Custom API Token

Follow these steps to create a token with the necessary permissions:

1. **Log in to Cloudflare** and navigate to your profile by clicking on your email or profile picture at the top right corner.
2. **Go to the 'API Tokens' tab** and click on the 'Create Token' button.
3. **Use the 'Create Custom Token' option** to start the token creation process.
4. **Configure your token** with the following permissions for the script to function properly:
   - **Permissions Needed:**
     - Zone.Zone: Read
     - Zone.DNS: Edit
5. **Set the Zone Resources** to include all zones or specify the zones you wish to manage with this token.
6. **Complete the token creation** by following the prompts and then **copy the generated token** to a secure location.

### Finding Your Zone ID

Your Zone ID is unique to your domain and is required by the script to identify which domain's DNS records to manage.

1. **Navigate to the Cloudflare dashboard** and select the domain you're working with.
2. Scroll down on the domain overview page. **Your Zone ID is listed at the bottom right** of the page.
3. **Copy the Zone ID** and keep it handy for the script.

### Installing the Requests Library

The script uses the `requests` library to make HTTP requests to the Cloudflare API. Install it using `pip`:

```sh
pip install requests
```

### Running the Script

With your API token, Zone ID, and requests library ready, you're set to run the script. Remember to replace the placeholder values in the script with your actual API token and Zone ID.

```sh
python script.py
```