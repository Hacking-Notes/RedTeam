--- ---

<h2>Windows</h2>

**Method 1: Clear Windows Event Logs Using Event Viewer**

Press the Windows + R keys to open the Run dialog, type **eventvwr.msc** and click OK to [open Event Viewer](https://www.top-password.com/blog/7-ways-to-access-event-viewer-in-windows-10/).

![](https://www.top-password.com/blog/wp-content/uploads/2020/08/eventvwr.png)

On the left sidebar of Event Viewer, expand “Windows Logs” and right-click one of the events categories, then select **Clear Log** from the menu that comes up.

![](https://www.top-password.com/blog/wp-content/uploads/2020/08/clear-log-from-event-viewer.png)

Click either the “**Save and Clear**” or the **Clear** button to confirm.

![](https://www.top-password.com/blog/wp-content/uploads/2020/08/save-event-logs-before-clearing.png)

The event logs will be cleared immediately.

---

**Method 2: Clear Windows Event Logs Using Command Prompt**

[Open an elevated Command Prompt window](https://www.top-password.com/blog/open-elevated-command-prompt-from-standard-user-in-windows/). Copy and paste the following command into the Command Prompt, and then hit Enter.  
`for /F "tokens=*" %1 in ('wevtutil.exe el') DO wevtutil.exe cl "%1"`

![](https://www.top-password.com/blog/wp-content/uploads/2020/08/clear-windows-event-logs-via-cmd.png)

This will delete all types of Windows event logs at once.

**Method 3: Clear Windows Event Logs Using PowerShell**

Press the Windows logo key + X to open the Quick Link menu, and then click on “**Windows PowerShell (Admin)**“.

![](https://www.top-password.com/blog/wp-content/uploads/2017/06/windows-powershell-admin.png)

To clear all event logs in Windows 10, just enter the below command and press Enter.  
`Get-EventLog -LogName * | ForEach { Clear-EventLog $_.Log }`

![](https://www.top-password.com/blog/wp-content/uploads/2020/08/clear-windows-event-logs-via-powershell.png)

That’s it!