terraform {
  backend "s3" {
    bucket = "my-project-tfstate"
    key    = "tfstate"
    region = "eu-west-1"
  }
}
