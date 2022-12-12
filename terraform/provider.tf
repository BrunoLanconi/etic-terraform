provider "aws" {
  region = local.aws_region

  default_tags {
    tags = {
      author = local.author
      mail = local.author_mail
      app_name = local.app_name
    }
  }
}