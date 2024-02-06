# CLI password generator and manager.

## Introduction to the CLI Password Generator

The CLI (Command Line Interface) password generator is a tool designed to simplify the management and generation of secure passwords for various online accounts. It operates through a series of commands issued in a terminal or command prompt, providing users with a straightforward method to create, store, and retrieve passwords securely.

## Key Features:

**Password Storage:** The generator allows users to securely store their login credentials for different websites or services. By saving usernames and passwords within the tool, users can avoid the need to remember multiple complex passwords or resort to less secure practices such as using the same password across multiple platforms.

**Password Generation:** For added security, the generator can automatically create strong, randomized passwords. Users have the option to let the tool generate a password for them or input their own if they prefer.

**Search Functionality:** The generator includes a search feature, enabling users to quickly retrieve their stored credentials for a specific website or service by providing its domain name.

**Password Deletion:** Should the need arise, users can easily delete stored credentials for a particular website or service, enhancing control over their stored data.

## How It Works:

Users interact with the generator through a series of commands entered into the terminal or command prompt.
Commands such as show, search, save, and delete are used to perform various actions like displaying all stored passwords, searching for credentials of a specific website, saving new credentials, and deleting existing ones.
The generator ensures the security of stored passwords by employing encryption and other security measures, safeguarding sensitive user data from unauthorized access.


## Usage:

1. **To show all passwords:**
   $ password-manager show

2. **To search for credentials of a specific website:**
   $ password-manager search website.com

3. **To save credentials for a website:**
   - If you have a password you want to use:
     $ password-manager save website.com user@email.com your_password
   - If you want to generate a strong password:
     $ password-manager save website.com user@email.com

4. **To delete credentials for a website:**
   $ password-manager delete website.com


