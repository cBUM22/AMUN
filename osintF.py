import dns.resolver as dnsr
import dns.exception
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import socket
from bs4 import BeautifulSoup
import time

DNS_Services = []
service_check = ["A", "AAAA", "MX", "NS", "CNAME", "TXT"]

def update_dns_data(ASN, target_domain):
    print(f"\n\033[33m---------- DNS data for {target_domain} ----------")
    hosts = [socket.gethostbyname(target_domain)]
    print("HOST IP:", hosts)
    print("\nDNS Records:")
    for record in DNS_Services:
        for key, values in record.items():
            for v in values:
                print(f'  {key}: r"{v}"\n')
    asn_number = ASN.split(" | ")[0] if ASN else ""
    asn_name = ASN.split(" | ")[-1] if ASN else ""
    print("\nASN:", asn_number)
    print("\nASN Name:", asn_name)
    print("----------------------------------\n")

def get_info(domain_info):
    DNS_Services.clear()
    resolver = dnsr.Resolver()
    resolver.timeout = 10
    resolver.lifetime = 20
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']

    for i in service_check:
        try:
            find_DNS_services = resolver.resolve(domain_info, i)
            DNS_Services.append({i: [r.to_text() for r in find_DNS_services]})
            print(f"{i} record found for {domain_info}")

        except dns.resolver.NoAnswer:
            print(f"No {i} record found for {domain_info}")
            
            print(f"\n\033[33m---------- DNS data for {domain_info} ----------")
            hosts = [socket.gethostbyname(domain_info)]
            print("HOST IP:", hosts)
            print("\nDNS Records:")
            for record in DNS_Services:
                for key, values in record.items():
                    for v in values:
                        print(f'  {key}: r"{v}"\n')
            asn_number = "NULL"
            asn_name = "NULL"
            print("\nASN:", asn_number)
            print("\nASN Name:", asn_name)
            print("----------------------------------\n")
            break

        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain_info} does not exist")
            return
        
        except dns.exception.Timeout:
            print(f"Timeout while resolving {i} for {domain_info}\n\033[31mTRYING AGAIN USING DNSDumpster")
            options = Options()
            options.add_argument("--headless")
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)

            try:
                driver.get("https://dnsdumpster.com/")
                time.sleep(3)
                box = driver.find_element(By.XPATH, './/input[@id="target"]')
                box.send_keys(domain_info)
                start_button = driver.find_element(By.XPATH, '//button[contains(text(), "Search")]')
                start_button.click()
                time.sleep(10)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                sections = soup.find_all("p")
                for p in sections:
                    table = p.find_next_sibling("table")
                    if table:
                        print(f"\n\033[35m=== {p.get_text(strip=True)} ===")
                        headers = [th.get_text(strip=True) for th in table.find_all("th")]
                        if headers:
                            print("\t".join(headers))
                        tbody = table.find("tbody")
                        if tbody:
                            for row in tbody.find_all("tr"):
                                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                                print("\t".join(cells))
            finally:
                driver.quit()
        except Exception as e:
            print(f"Error resolving {i} for {domain_info}: {e}")

    try:
        reversed_ip = '.'.join(reversed(socket.gethostbyname(domain_info).split('.')))
        query = f"{reversed_ip}.origin.asn.cymru.com"
        answer = resolver.resolve(query, 'TXT')
        data = str(answer[0]).strip('"')
        print(f"\nASN Data for {domain_info}: {data}\n")
        update_dns_data(data, domain_info)
    except Exception as e:
        print(f"Could not retrieve ASN data for {domain_info}: {e}")

def get_target_domain(target_domain):
    get_info(target_domain)
