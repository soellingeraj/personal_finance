
# coding: utf-8

# In[96]:


import pandas as pd
from scipy.optimize import linprog
from typing import Dict, List
from uuid import uuid4 as Uuid4
from datetime import Date


# In[153]:


class SparseDate():
    
    def __init__(self, year: int = 0, month: int = 0, day: int = 0,
                 hour: int = 0, minute: int = 0, second: int = 0):
        
        self.year   = year
        self.month  = month
        self.day    = day
        self.hour   = hour
        self.minute = minute
        self.second = second
    
    def __repr__(self):
        
        return str(self.get())
    
    @classmethod
    def from_string(cls, datestring: str, 
                    dateformat: str):
        
        temp   = datetime.strptime(datestring, dateformat)
        year   = temp.year
        month  = temp.month
        day    = temp.day
        hour   = temp.hour
        minute = temp.minute
        second = temp.second
        return cls(year, month, day, hour, minute, second)
    
    @classmethod
    def from_datetime(cls, dt_obj: datetime):
        
        year   = dt_obj.year
        month  = dt_obj.month
        day    = dt_obj.day
        hour   = dt_obj.hour
        minute = dt_obj.minute
        second = dt_obj.second
        return cls(year, month, day, hour, minute, second)
    
    def get(self):
        
        dtm = self._get_datetime()
        
        if dtm == None:
        
            return self.get_str()
        
        else:
            
            return dtm
        
    def get_str(self):
        
        return '{0:02d}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}'                     .format(self.year, self.month, self.day,
                            self.hour, self.minute, self.second)
    
    def _get_datetime(self):
        
        if int(self.year) == 0 or int(self.month) == 0 or int(self.day) == 0:
           
            return None
        
        else: 
             
            return datetime(self.year, self.month, self.day, 
                            self.hour, self.minute, self.second)
        
class DateInterval():
    
    def __init__(self, start: SparseDate, end: SparseDate):
        
        self.start = start
        self.end   = end


# In[152]:


datetime.strptime(str(datetime.now()))


# In[138]:


class Server():
    
    def __init__(self):
        
        self.item_manager = ItemManager()

class Transaction():
    
    def __init__(self, flow: Flow, date: SparseDate,
                 value: float, currency: str):
        
        self.flow     = flow
        self.date     = date
        self.value    = value
        self.currency = currency
        

class Item():
    
    def __init__(self, ident: Uuid4, name: str, 
                 initial_value: float):
        
        self.id   = ident
        self.name = name
        self.initial_value = initial_value
        self.expenses = Dict[str, Expense]
        self.incomes  = Dict[str, Income]


class Asset(Item):
    
    def __init__(self, name: str, value: float, initial_value: float):
        
        self.market_value      = initial_value
        self.market_value_date = SparseDate.from_datetime(datetime.now())
        self.incomes           = Dict[str, Income]
        self.liabilities       = Dict[str, Liability]
        self.depreciation      = Dict[SparseDate, float]
        
        super().__init__(ident, name)

class Liability(Item):
    
    def __init__(self, name: str, ident: str, 
                 initial_value: float):
 
        self.balance      = initial_value
        self.balance_date = SparseDate.from_datetime(datetime.now())
        self.payments     = Dict[SparseDate, Expense]
        self.outlays      = Dict[SparseDate, float]
        self.collaterals  = Dict[str, Asset]
        
        super().__init__(name, ident, initial_value)

    def apply_payment(self, date, amount: float, 
                      dateformat: str = None):
            
        self.outlays[SparseDate.from_string(date, dateformat)] = amount
        
class RealEstate(Asset):
    
    def __init__(self, name: str, initial_value: float, value: float = 0.0, 
                 downpmt_pct: float = 0.0, transx_tax_pct: float = 0.0,
                 transx_fee_pct: float = 0.0, insurance_prem_pct: float = 0.0):
        
        self.name               = name
        self.downpmt_pct        = downpmt_pct
        self.transx_tax_pct     = transx_tax_pct
        self.transx_fee_pct     = transx_fee_pct
        self.insurance_prem_pct = insurance_prem_pct
        
        super().__init__(name, value, initial_value)
        
        
class Stream():
    
    # TODO
    def __init__(self, name: str, date: datetime, #):
        
        self.name         = name
        self.date         = SparseDate.from_datetime(date)
        self.value        = value
        self.frequency    = frequency
        self.category     = category
        self.is_fulfilled = 
    
class Income(Stream):
    
    def __init__(self, name: str, value: float, 
                 frequency: str, category: str):
        
        super().__init__(name, value, frequency,
                         category)

class Expense(Stream):
    
    def __init__(self, name: str, value: float, 
                 frequency: str, category: str):
        
        super().__init__(name, value, frequency,
                         category)
        
class ItemManager():
    
    def __init__(self):
        
        self.items = Dict[str, Expense]
    
    def add_thing(self, item: Item):
        
        if expense.name not in self.items:
            
            self.items[expense.name] = item
            
        else:
            
            raise ValueError('An expense with the name', expense.name,
                             'already exists in ExpenseManager.')
    
    def get_item(self, name: str):
        
        return self.items[name]    


# In[35]:


if __name__ == '__main__':
    
    SESSION = Server()
    
    tx_taxes_perc = .10
    down = 0.20
    owner_ins_pct = 200.0 / 135000
    
    exps = [Expense('selling_price', 300000.0, 'one-time-proj', 'house'),
            Expense('transaction_tax', tx_taxes_perc * amt_adjuster(selling_price), 
                    'one-time-proj'),
            Expense('home-owner-insurance', owner_ins_pct * amt_adjuster(selling_price), 
                    'annual-proj'),
            Expense('property-taxes', 250.0, 'annual-proj'),
            Expense('mortgage-insurance', 66.0, 'annual-proj'),
            Expense('home-maintenance', 50.0, 'month-proj'),
            Expense('down-payment', P * down, 'one-time-proj'),
            Expense(),
    

# inputs (amount, period: 0=one time, >0=in months)

# house
mortg_insur   = ()
maintenance   = ()
renovation    = (10000.0, 'one-time')
down_pmt_pct  = 0.20
down_pmt_amt  = (down_pmt_pct * amt_adjuster(selling_price), 'one-time')

# Utilities
hot_water     = (50.0,  'monthly')
water         = (50.0,  'monthly')
electricity   = (50.0,  'monthly')
gas           = (50.0,  'monthly')
cmty_fee      = (250.0, 'monthly')

# Loan params
dur_yrs       = 30.0
pds_yr        = 12
interest_rate = 0.025
is_ren_cash   = True
nat_grwth_ann = 0.06
pct_renov_out = 0.80


# In[36]:


def compute_payment_tables(pmt, dur_yrs, pds_yr, p, down_pmt, r, optim=True):
    
    out = []
    
    bal = p - down_pmt
    
    out.append({
            'new_balance': bal,
            'interest_paid': 0.0,
            'interest_cumd': 0.0,
            'principl_paid': 0.0,
            'principl_cumd': 0.0,
            'utility+hoa'  : 0.0,
            'cash_required': amt_adjuster(hot_water) +
                             amt_adjuster(hot_water) +
                             amt_adjuster(hot_water)
        })
    
    for i in range(int(pds_yr * dur_yrs)):
        
        interest = bal * (r / 12.0)
        
        principl = pmt - interest
        
        bal = bal + interest - pmt
        
        out.append({
            'new_balance': bal,
            'interest_paid': interest,
            'interest_cumd': out[-1]['interest_cumd'] + interest,
            'principl_paid': principl,
            'principl_cumd': out[-1]['principl_paid'] + principl,
            'utilities'    : amt_adjuster(hot_water) + \
                             amt_adjuster(water) + \
                             amt_adjuster(electricity) + \
                             amt_adjuster(gas) + \
                             amt_adjuster(gas) + \
            'hoa'          :
            
        })
    
    if optim:
        
        return out[-1]['new_balance']
    
    else:
        
        return pd.DataFrame(out)
    


# In[62]:


bal = 1001.0
pmt = 100
dec = 10
eps = 0.001
switch = 1

def increment(dec, switch):
    
    global pmt
    
    if switch:
        
        pmt += dec
        
    else:
        
        pmt -= dec

while abs(bal) > eps:
        
    increment(dec, True)
    
    bal = compute_payment_tables(pmt, dur_yrs, pds_yr, 
                                 amt_adjuster(selling_price), 
                                 amt_adjuster(down_pmt), 
                                 interest_rate)
    
    if bal < 0:
        
        increment(dec, False)
        
        dec = dec / 2

schedule = compute_payment_tables(pmt, dur_yrs, pds_yr, 
                                  amt_adjuster(selling_price), 
                                  amt_adjuster(down_pmt), 
                                  interest_rate, False)


# In[65]:


schedule


# In[64]:


#sum (from 1 to N): bal - x[0]
compute_payment_tables(pmt, dur_yrs, pds_yr, 
                       amt_adjuster(selling_price), 
                       amt_adjuster(down_pmt), 
                       interest_rate)


# In[49]:


iterations_hat = 0

while _w_in_pd_iter != iterations:
    
    #print('--- new run ---')
    #print('payment', pmt_hat)
    #print('---------------')
    
    pmt_hat -= 100.00

    _w_in_pd_iter = 0
    
    b = apply_payments(pmt_hat, P, r)
        


# In[ ]:


"""Model

Total_Outlay_per_Year = recoverable + non-recoverable

recoverable
  * equity-in
  * equity-growth
  * renovation
  
non-recoverable
  * insurance
  * taxes
  * community dues
  * utilities
  
loan solver:

minimize: pmt

subject to: pmt

"""

