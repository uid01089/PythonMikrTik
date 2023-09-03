import getpass
import tkinter as tk
from tkinter import ttk

from MikrotikRouter import MikrotikRouter

def main() -> None:
    # Get the password from the user
    password = getpass.getpass(prompt='Password: ')

    # Create the main window
    root = tk.Tk()
    root.title('WiFi')

    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=('mac', 'ip', 'hostname', 'last_seen', 'rxRate', 'txRate', 'accessPoint', 'interface', 'signalStrength', 'activity', 'lastActivity'), show='tree')
    
    # Define headings for the Treeview
    tree.heading('mac', text='First mac')
    tree.heading('ip', text='ip')
    tree.heading('hostname', text='hostname')
    tree.heading('last_seen', text='last_seen')
    tree.heading('rxRate', text='rxRate')
    tree.heading('txRate', text='txRate')
    tree.heading('accessPoint', text='accessPoint')
    tree.heading('interface', text='interface')
    tree.heading('signalStrength', text='signalStrength')
    tree.heading('activity', text='activity')
    tree.heading('lastActivity', text='lastActivity')

    # Define columns for the Treeview
    tree.column('mac', width=100, anchor=tk.W)
    tree.column('ip', width=100, anchor=tk.W)
    tree.column('hostname', width=200, anchor=tk.CENTER)    
    tree.column('last_seen', width=100, anchor=tk.W)
    tree.column('rxRate', width=100, anchor=tk.W)
    tree.column('txRate', width=200, anchor=tk.CENTER)    
    tree.column('interface', width=100, anchor=tk.W)
    tree.column('activity', width=200, anchor=tk.CENTER)    
    
    # Create a MikrotikRouter object
    centralRouter = MikrotikRouter("10.10.30.1", "admin", password)
    
    # Get lease, DNS, and activity information from the router
    leases = centralRouter.getLeases()
    leasesByMac = leasesSortedByMac(leases)

    dns = centralRouter.getDns()
    dnsByMac = dnsSortedByAddress(dns)

    activities = centralRouter.getActivities()
    activitiesByMac = activitiesSortedByMac(activities)

    # Get information about the access points
    accessPoints = centralRouter.getNeighbors()

    # Loop through the access points and add them to the Treeview
    for accessPoint in accessPoints:
        accessPointSection = tree.insert('', tk.END, text=accessPoint.getIdentity())
        
        registrationTable = accessPoint.getWiFiRegistrationTable()
        for reg in registrationTable:
            macAddress = reg["mac-address"]

            if macAddress in leasesByMac:
                lastSeen = leasesByMac[macAddress]['last-seen']
            else:
                lastSeen = "Not available"

            if macAddress in activitiesByMac:
                ip = activitiesByMac[macAddress]['ip-address']
                hostname = activitiesByMac[macAddress]['name']
                activity = activitiesByMac[macAddress]['activity']
            else:
                ip = "Not available"
                hostname = "Not available"
                activity = "No activity"

            line = []
            line.append(macAddress)
            line.append(ip)
            line.append(hostname)
            line.append(lastSeen)
            line.append(reg["rx-rate"])
            line.append(reg["tx-rate"])
            line.append(reg["interface"])
            line.append(reg["signal-strength"])
            line.append(activity)
            line.append(reg["last-activity"])
            tree.insert(accessPointSection, tk.END, values=line)
            
    # Add a scrollbar to the Treeview
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(fill='y', side='right')

    # Pack the Treeview and start the main loop
    tree.pack(fill='both', expand=True)
    root.mainloop()

# Function to sort leases by MAC address
def leasesSortedByMac(leases: list) -> dict:
    leasesByMac = {}
    for lease in leases:
        leasesByMac[lease['mac-address']] = lease
    return leasesByMac

# Function to sort DNS entries by address
def dnsSortedByAddress(dns: list) -> dict:
    dnsByAddress = {}
    for entry in dns:
        dnsByAddress[entry['address']] = entry
    return dnsByAddress

# Function to sort activities by MAC address
def activitiesSortedByMac(activities: list) -> dict:
    activitiesByMac = {}
    for activity in activities:
        activitiesByMac[activity['mac-address']] = activity
    return activitiesByMac

# Start the program
if __name__ == '__main__':
    main()
