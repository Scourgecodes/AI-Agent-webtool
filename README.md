# Web Tool AI Agent (webtool.py)

An interactive, terminal-based Python AI agent built to check remote website availability and parse live API payloads over the internet. This tool runs entirely using native standard libraries, eliminating the need for external package dependencies.

---

## Technical Overview

The application features an interactive loop that acts as an automated agent interface. It takes network commands, formats unstructured text entries, performs secure HTTP GET requests, and decodes incoming byte streams into readable Python dictionary structures.

### Key Features
* Live Website Status Check: Takes any custom URL or falls back to a default web host, sends a request header, and catches the active status response code from the remote server.
* REST API Connection: Queries a public test API endpoint, retrieves raw server bytes, and structuralizes JSON key-value data cleanly for the user interface.
* Error Protection: Built-in exception handling to prevent software crashes if a URL is broken, typed incorrectly, or if the system loses internet connection.

---

## Technology Stack

* Language Platform: Python 3
* Core Built-in Modules:
  * urllib.request — Opens remote URLs and processes online data transactions.
  * json — Parses raw incoming byte arrays into standard Python dictionaries.

---

## Installation & Setup

1. Open your Anaconda Prompt or standard command line terminal.
2. Navigate directly to your local workspace directory using the change directory command:
   cd OneDrive\Desktop\AI_Agents
3. Run the interactive terminal script using your Python interpreter:
   python webtool.py

---

## System Commands Guide

Once the terminal loop is running, enter any of the specific interactive parameters below:

### 1. Default Connectivity Check
Tests default connection paths to global network hosts.
* Command: check site
* Expected Output: Result -> https://www.google.com is ONLINE (Status Code: 200)

### 2. Custom Domain Verification
Tests network connections for specific website domains.
* Command: check site, github.com
* Expected Output: Result -> https://github.com is ONLINE (Status Code: 200)

### 3. API Payload Data Fetching
Retrieves active dummy data payloads from an online mock server.
* Command: fetch api
* Expected Output: Result -> API Connected! Internet Task Title: 'delectus aut autem'

### 4. Close the Agent Process
Safely terminates the interactive command execution sequence.
* Command: exit
* Expected Output: Shutting down Web Tool. Goodbye!

---

## Code Execution Flow

[User Input] ➔ [Command String Parser] ➔ [urllib HTTP Request] ➔ [JSON Dictionary Decode] ➔ [Terminal Output Response]

Every request uses strict request timeouts (5 seconds) to ensure that the script does not hang indefinitely if a website fails to respond.
