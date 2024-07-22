# Create variables 

$IP = "192.168.1.10"
$MaskBits = 24 #CIDR Notation
$Gateway = "192.168.1.1"
$IPType = "IPv4"
$dnsPrimary = "192.168.1.1"
$dnsSecondary = "8.8.8.8"

$domainName = "NET2Grid.com"
$domainNetBIOSName = "NET2Grid"
$domainAdminPassword = ConvertTo-SecureString "NET2Grid_123" -AsPlainText -Force
$databasepath = "C:\Windows\NTDS"
$logpath = "C:\Windows\NTDS"
$sysvolpath = "C:\Windows\SYSVOL"

# Retrieves the network adapter that is up and saves it to the variable "$adapter"
$adapter = Get-NetAdapter | ? {$_.Status -eq "up"}

# Clears our adapter of IPv4 and default gateway configuration
if (($adapter | Get-NetIPConfiguration).IPv4Address.IPAddress){
 $adapter | Remove-NetIPAddress -AddressFamily $IPType -Confirm:$false
}
If (($adapter | Get-NetIPConfiguration).Ipv4DefaultGateway) {
 $adapter | Remove-NetRoute -AddressFamily $IPType -Confirm:$false
}

#Configure static IPv4 Address 
$adapter | New-NetIPAddress `
-AddressFamily $IPType `-IPAddress $IP `-PrefixLength $MaskBits `
-DefaultGateway $Gateway 

# Clears the DNS server configuration on the adapter
Set-DnsClientServerAddress `
-InterfaceAlias "Ethernet" `
-ResetServerAddresses 

# Configures new DNS Server for the adapter
Set-DnsClientServerAddress `
-InterfaceAlias "Ethernet" `
-ServerAddresses ($dnsPrimary, $dnsSecondary) 

# Installs AD-Domain-Services
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools

# Promotes server to domain controller and configures a new forest in the Active Directory
# Import the Active Directory module
Import-Module ADDSDeployment

# Promote server to domain controller and configure a new forest
Install-ADDSForest `
    -DomainName $domainName `
    -DomainNetBiosName $domainNetBIOSName `
    -ForestMode WinThreshold `
    -DomainMode WinThreshold `
    -CreateDnsDelegation:$false `
    -DatabasePath $databasepath `
    -LogPath $logpath `
    -SysvolPath $sysvolpath `
    -Force:$true `
    -NoRebootOnCompletion:$true `
    -SafeModeAdministratorPassword $domainAdminPassword

Restart-Computer 



