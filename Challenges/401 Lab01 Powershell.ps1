# Set automatic update settings
$automaticUpdateSettings = @{
    "AUOptions" = 4  # 4 - Automatically download and schedule installation
    "ScheduledInstallDay" = 0  # 0 - Every day
    "ScheduledInstallTime" = 3  # 3 - 3:00 AM (adjust as needed)
}

# Set Windows Update registry keys
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\" -Name "AUOptions" -Value $automaticUpdateSettings["AUOptions"]
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\" -Name "ScheduledInstallDay" -Value $automaticUpdateSettings["ScheduledInstallDay"]
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\" -Name "ScheduledInstallTime" -Value $automaticUpdateSettings["ScheduledInstallTime"]

# Restart Windows Update service to apply changes
Restart-Service -Name wuauserv -Force