variable "app_name" {
  type = string
  description = "A string representing the APP name"
  default = "my-project"
}

variable "aws_region" {
  type = string
  description = "A string representing the AWS region"
  default = "eu-west-1"
}

variable "author" {
  type = string
  description = "A string representing the author name"
  default = "Bruno Lanconi"
}

variable "author_mail" {
  type = string
  description = "A string representing the author mail"
  default = "contato@brunolanconi.com.br"
}
