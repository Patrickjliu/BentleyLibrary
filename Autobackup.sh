#!/bin/bash

set -x

# Set the backup directory
BACKUP_DIR="/Users/patrick/Coding/BentleyLibrary"

# Get the current date in YYYY-MM-DD format
DATE=$(date +"%Y-%m-%d")

# Set the backup file name
BACKUP_FILE="${BACKUP_DIR}/BentleyLibraryBackup_${DATE}.sql"

# Perform the backup
mysqldump -u root -p BentleyLibrary > $BACKUP_FILE
