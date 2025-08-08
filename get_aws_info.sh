#!/bin/bash
# Print AWS Account ID and Alias using AWS CLI

# Get AWS Account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Get AWS Account Alias
ACCOUNT_ALIAS=$(aws iam list-account-aliases --query 'AccountAliases[0]' --output text)

# Show results
echo "AWS Account ID: $ACCOUNT_ID"
echo "AWS Account Alias: $ACCOUNT_ALIAS"
