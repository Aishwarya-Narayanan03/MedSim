# main.tf - Terraform for GCP infrastructure
provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "medsim_data" {
  name     = "medsim-data-bucket"
  location = var.region
}

resource "google_cloud_run_service" "backend" {
  name     = "medsim-backend"
  location = var.region
  template {
    spec {
      containers {
        image = var.backend_image
      }
    }
  }
}

variable "project_id" {}
variable "region" { default = "europe-west1" }
variable "backend_image" {}
