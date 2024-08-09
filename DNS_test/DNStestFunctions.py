from scapy.all import *
import signal

def checkDNSresponse(DNSaddress, WebsiteDomain, DNSrecordType):
    def handler(signum, frame):
        raise RuntimeError
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    try:
        DNSresponse = sr1(IP(dst=DNSaddress)/UDP()/DNS(rd=1,qd=DNSQR(qname=WebsiteDomain,qtype=DNSrecordType)))
        match DNSrecordType:
            case "A":
                return {f"{i.rdata}" for i in DNSresponse.an}
            case "AAAA":
                return {f"{i.rdata}" for i in DNSresponse.an}
            case "MX":
                return {f"{i.exchange} {i.preference}" for i in DNSresponse.an}
            case "CNAME":
                return {f"{i.rrname}" for i in DNSresponse.ns}
            case "NS":
                return {f"{i.rdata}" for i in DNSresponse.an}
            case "SOA":
                return {f"{i.rrname} {i.mname} {i.rname} {i.serial} {i.refresh} {i.retry} {i.expire} {i.minimum}" for i in DNSresponse.an}
            case "CAA":
                return {f"{i.rrname} {i.rdata}" for i in DNSresponse.an}
            case "PTR":
                return {f"{i.rdata}" for i in DNSresponse.an}
            case _:
                return "Error: something went wrong"
        signal.alarm(0)
    except RuntimeError:
        return "Runtime error has occured"
    except IndexError:
        return "Error: provided website domain is incorrect, missing, or doesn't exist."
    except KeyError:
        return "Error: provided DNS record type is incorrect, missing, or doesn't exist."
    except (UnicodeError, OSError, AttributeError, socket.gaierror):
        return "Error: provided DNS address is incorrect or missing."

def checkForMultipleRequests(DNSaddress, WebsiteDomain, DNSrecordType, expectedResponse, amountOfRequests):
    def handler(signum,frame):
        raise RuntimeError
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(amountOfRequests)
    amountOfCorrectResponses = 0
    try:
        for i in range(0,amountOfRequests):
            checkDNSresponse(DNSaddress, WebsiteDomain, DNSrecordType)
            if checkDNSresponse(DNSaddress, WebsiteDomain, DNSrecordType) == expectedResponse:
                amountOfCorrectResponses += 1
            else:
                continue
        signal.alarm(0)
        return amountOfCorrectResponses
    except RuntimeError:
        amountOfCorrectResponses = 0
        return amountOfCorrectResponses
    except IndexError:
        return "Error: provided website domain is incorrect, missing, or doesn't exist."
    except KeyError:
        return "Error: provided DNS record type is incorrect, missing, or doesn't exist."
    except (UnicodeError, OSError, AttributeError, socket.gaierror):
        return "Error: provided DNS address is incorrect or missing."

#print(checkDNSresponse("8...4", " ", "A"))
#print(checkDNSresponse("8.8.4.4", "yahoo.com", "D"))
#print(checkForMultipleRequests("8.8.4.4", "x-kom.pl", ".", {'104.20.71.117', '104.20.72.117'}, 100))
