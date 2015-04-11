# vacuumpot (exfiltrating honeypot)
sucking up packets and spitting them outbound

sniff and spit style (http://www.andlabs.org/tools/SniffnSpit/SniffnSpit.html) network proxy 
to capture and redirect packets to new destination (internal / external)
relying on infrastructure to routing 

spoof to hide, no IP address



client:
  wrappers for covert exfiltration
  wrappers for encrypting payloads

server:
  modified kernel does not reply to malformed packets
  iptables redirect to listener


more information to come 
