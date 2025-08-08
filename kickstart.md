# Project Description

## Context

This is an IaC project to build infraestructure in AWS Cloud provider using serverless framework 3.38.0 and AWS Cloudformation, the goal is build a base pipeline to start others pipelines, the entry point for this proyect is serverless.yml in folder root.

## The project structure

Considere the next project structure:


- infra (folder)
    pipeline.yml : Cloudformation code to build a pipeline to deploy de infraestruture in this folder
    - buckets (folder)
        artifact.yml :  serverless s3 bucket required for this infra
    - vpc (folder): Contains the basic cloudformation files configuration for vpc (vpc, subnets, nat, internet gateway, routables, acls )
    serverless.yml : file to build the above infrasture described at the end of the file
    buildspec.yml: called from pipeline to build de infra and execute de serverless.yml in current folder
- kickstart (folder)
    pipeline.yml : Cloudformation code to build a pipeline with 2 stage
buildspec.yml: buildspect for codebuild called in kickstart/pipeline is responsible to call serverless.yml file in root
serverless.yml: serverless file to config de enviroment in aws account, role an basic custom configs, and the end of the file call the build the kicstart/pipeline and infra/pipeline 