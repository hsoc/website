variable "profile" {
  description = "Name of your profile inside ~/.aws/credentials"
}

variable "application_name" {
  description = "Web application name"
}

variable "application_description" {
  description = "Description of Elastic Beanstalk application"
}

variable "region" {
  description = "Defines at which AWS region your app will be deployed"
}

variable "rds_username" {
  description = "Defines AWS RDS db username"
}

variable "rds_password" {
  description = "Defines AWS RDS db password"
}

variable "secret_key" {
  description = "Defines Django secret key"
}

variable "sentry_dsn" {
  description = "Defines Sentry data source name"
}

variable "okthess_aws_access_key_id" {
  description = "Defines AWS access key id"
}

variable "okthess_aws_secret_access_key" {
  description = "Defines AWS secret access key"
}

variable "okthess_aws_ses_user" {
  description = "Defines AWS SMTP username"
}

variable "okthess_aws_ses_password" {
  description = "Defines AWS SMTP password"
}
