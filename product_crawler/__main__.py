from product_crawler.service.monitoring_product_service import MonitoringProductService


def main():
    MonitoringProductService.start_monitoring()


if __name__ == "__main__":
    main()
