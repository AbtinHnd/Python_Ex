# Linux-Like Command Line Interface (CLI)

## Overview

This project is a custom implementation of a Linux-like Command Line Interface (CLI) in Python, providing essential file manipulation and navigation commands. It mimics the behavior of common Linux commands and offers additional logging functionality. This project can be used to explore how CLI commands are processed and executed in a simple operating environment.

## Features

- **Navigation Commands**:
  - `cd [directory]`: Change the current working directory.
  - `ls [options]`: List files and directories.
  
- **File Commands**:
  - `mkdir [directory]`: Create a new directory.
  - `rmdir [directory]`: Remove an empty directory.
  - `rmr [file/directory]`: Recursively remove files or directories.
  - `cp [source] [destination]`: Copy files or directories.
  - `mv [source] [destination]`: Move or rename files or directories.
  - `cat [file]`: Display the contents of a file.

- **System Commands**:
  - `log`: Display or manage system logs.
  - `find [filename]`: Search for files within the current directory tree.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/linux-like-cli.git
