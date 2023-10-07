
import whois

domain = input('Enter domain name: ')
whois_info = whois.whois(domain)

print(whois_info)