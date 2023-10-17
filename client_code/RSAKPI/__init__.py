from ._anvil_designer import RSAKPITemplate
import anvil.server

class KPITRANS():
  #Parameters in.
  month = 0
  year = 0

  #Parameters out
  critical = 0
  high = 0
  normal = 0
  low = 0
  trivial = 0
  service_requests = 0
  system_logs = 0
  dvcsd_contacts = 0
  tickets_less_than_ten_days = 0
  tickets_more_than_sixty = 0

  openSifters = 0
  reopenedSifters = 0
  followupSifters = 0
  resolvedSifters = 0
  closedSifters = 0
  totalSifters = 0
  percentage_incidents_in_sla = 0


class RSAKPI(RSAKPITemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def exit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    return

  def sifter_btn_click(self, **event_args):
    """This method is called when the sifter button is clicked"""
    # Passing self give a serialisation error
    # As with OpenROAD JSON does not support by reference parameters
    results = KPITRANS
    KPITRANS.month = int(self.month.selected_value)
    KPITRANS.month = int(self.year.selected_value)
    KPITRANS = anvil.server.call('GetRSASIFTER', KPITRANS)

      


  
  def save_btn_click(self, **event_args):
    """This method is called when the save button is clicked"""
    with open('c:\\temp\\kpi_report_'+self.month.selected_value+'_'+self.year.selected_value+'.txt', 'a') as report:
        HC_NEWLINE = '\n'
        HC_TAB = '\t'
        report.write( 'RSA KPI Report for '+'Test Month' +HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( 'Incident Management'+HC_NEWLINE )
        report.write( HC_NEWLINE )
        report.write( '1. Number of Incidents in month'+HC_NEWLINE )
  
        report.write( HC_NEWLINE )
        report.write( 'Critical  ' + HC_TAB + str(self.critical.text) + HC_NEWLINE )
        report.write( 'High  '  + HC_TAB+HC_TAB + str(self.high.text) + HC_NEWLINE)	
        report.write( 'Normal  ' + HC_TAB + str(self.normal.text)+ HC_NEWLINE)
        report.write( 'Low  '  + HC_TAB+HC_TAB + str(self.low.text)+ HC_NEWLINE)
        report.write( 'Trivial  ' + HC_TAB + str(self.trivial.text)+ HC_NEWLINE)
  
        report.write( HC_NEWLINE +'Failed SLAs on SIFTER response time for: ' + HC_NEWLINE)
  
        if len(self.failedresponse) == 0:
            report.write( HC_NEWLINE +'None.' + HC_NEWLINE)
        else:
            report.write( HC_NEWLINE )
            for kpifailure in self.failedresponse:
                report.write( 'SIFTER  ' + HC_TAB + kpifailure + HC_NEWLINE )
  
        report.write( HC_NEWLINE )
        report.write( '1.1 SIFTER Volumes'+HC_NEWLINE )
  
        report.write( HC_NEWLINE )
        report.write( 'Open' + HC_TAB + HC_TAB+ str(self.open.text) + HC_NEWLINE )
        report.write( 'Reopened'  + HC_TAB + str(self.reopened.text) + HC_NEWLINE)    
        report.write( 'Followup' + HC_TAB + str(self.followup.text)+ HC_NEWLINE)
        report.write( 'Resolved'  + HC_TAB + str(self.resolved.text)+ HC_NEWLINE)
        report.write( 'Closed' + HC_TAB +HC_TAB+ str(self.closed.text)+ HC_NEWLINE)    
        report.write( 'Total' + HC_TAB +HC_TAB+ str(self.total.text)+ HC_NEWLINE)    
  
        report.write( HC_NEWLINE )
        report.write( '2. Percentage of incidents that met service levels (where no dependance on DVCSD)' +HC_NEWLINE)
        report.write( HC_NEWLINE )    
        report.write( 'Percentage  ' + HC_TAB +  str(self.percentage_incidents_in_sla.text) + '%' +HC_NEWLINE )
        report.write( HC_NEWLINE )
        report.write( '3. First contact resolution rate' +HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( 'Not Applicable  All incidents raised through SIFTER'+HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( '4. Number of incident backlog/aged tickets less than 10 days old (where no dependency on DVCSD)' +HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( 'Tickets  ' + str(self.tickets_less_than_ten_days.text)+HC_NEWLINE)        
        report.write( HC_NEWLINE )
        report.write( '5. Unplanned Outages split into DVCSD and Vendor issues' +HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( 'Not Applicable, Production is managed by DVCSD'+HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( '6. Number of Service requests' +HC_NEWLINE)
        report.write( HC_NEWLINE )    
        report.write( 'Tickets  ' + str(self.service_requests.text)+HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( '7. Percentage of service requests that met service levels.' +HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( 'Not Applicable, There is no SLA for service requests'+HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( '8. Number of SR aged tickets 60 days (where no dependency on DVCSD)' +HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( 'Tickets  ' + str(self.tickets_more_than_sixty.text)+HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( '9. Number of issues identified from system logs' +HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( 'Tickets  ' + str(self.system_logs.text)+HC_NEWLINE)    
        report.write( HC_NEWLINE )        
        report.write( '10. Number of alerts/communications from DVCSD actioned' +HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( 'Tickets  ' + str(self.dvcsd_contacts.text)+HC_NEWLINE)        
        report.write( HC_NEWLINE )    
        report.write( '11. System up time clarify what is DVCSD and Vendor related on downtime.' +HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( 'Not Applicable' +HC_NEWLINE)                
  
        report.write( HC_NEWLINE )
        report.write( 'Release Management'+HC_NEWLINE )
        report.write( HC_NEWLINE )            
  
  
        report.write( '1. Hypercare Exit on deployments major releases - Exit of hypercare after 1 month dependent no P1 or P2 raised by customer/ business in the last 7 days.' +HC_NEWLINE)
        report.write( HC_NEWLINE )
        report.write( 'N/A' +     HC_NEWLINE )
        report.write( '2. Minor releases will have related hypercare of 2 weeks - no P1 or P2 raised by customer/business in the last 4 days to close that hypercare period.' +HC_NEWLINE)    
        report.write( HC_NEWLINE )
        report.write( 'N/A' + HC_NEWLINE )  
















