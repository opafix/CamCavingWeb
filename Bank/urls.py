from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('Entry/Create/', views.CreateEntry.as_view(), name='CreateEntry'),
    path('Entry/View/<slug:slug>', views.ViewEntry.as_view(), name='ViewEntry'),
    path('Entry/Edit/<slug:slug>', views.EditEntry.as_view(), name='EditEntry'),
    path('Entry/ToggleApprove/<slug:slug>', views.ToggleApproveEntry, name='ToggleApproveEntry'),
    path('Entry/Delete/<slug:slug>', views.DeleteEntry.as_view(), name='DeleteEntry'),

    path('Account/Create/', views.CreateAccount.as_view(), name='CreateAccount'),
    path('Account/List/', views.ListAccounts.as_view(), name='ListAccounts'),
    path('Account/View/<slug:slug>', views.ViewAccount.as_view(), name='ViewAccount'),
    path('Account/Edit/<slug:slug>', views.EditAccount.as_view(), name='EditAccount'),
    path('Account/Delete/<slug:slug>', views.DeleteAccount.as_view(), name='DeleteAccount'),

    path('Transaction/Create/', RedirectView.as_view(url='Creditor/'), name='CreateTransaction'),
    path('Transaction/Create/Creditor/', views.CreateTransactionCreditor.as_view(), name='CreateTransactionCreditor'),
    path('Transaction/Create/Debtor/', views.CreateTransactionDebtor.as_view(), name='CreateTransactionDebtor'),
    path('Transaction/Create/Data/', views.CreateTransactionData.as_view(), name='CreateTransactionData'),
    path('Transaction/Create/Action/', views.CreateTransactionAction, name='CreateTransactionAction'),
    path('Transaction/View/<slug:slug>', views.ViewTransaction.as_view(), name='ViewTransaction'),
    path('Transaction/Edit/Creditor/<slug:slug>', views.EditTransactionCreditor.as_view(), name='EditTransactionCreditor'),
    path('Transaction/Edit/Debtor/<slug:slug>', views.EditTransactionDebtor.as_view(), name='EditTransactionDebtor'),
    path('Transaction/Edit/Data/<slug:slug>', views.EditTransactionData.as_view(), name='EditTransactionData'),
    path('Transaction/Edit/Action/', views.EditTransactionAction, name='EditTransactionAction'),
    path('Transaction/ToggleApprove/<slug:slug>', views.ToggleApproveTransaction, name='ToggleApproveTransaction'),
    path('Transaction/Delete/<slug:slug>', views.DeleteTransaction.as_view(), name='DeleteTransaction'),

    path('TransactionGroup/Create/', RedirectView.as_view(url='Creditor/'), name='CreateTransactionGroup'),
    path('TransactionGroup/Create/Creditor/', views.CreateTransactionGroupCreditor.as_view(), name='CreateTransactionGroupCreditor'),
    path('TransactionGroup/Create/Debtor/', views.CreateTransactionGroupDebtor.as_view(), name='CreateTransactionGroupDebtor'),
    path('TransactionGroup/Create/Data/', views.CreateTransactionGroupData.as_view(), name='CreateTransactionGroupData'),
    path('TransactionGroup/Create/Action/', views.CreateTransactionGroupAction, name='CreateTransactionGroupAction'),
    path('TransactionGroup/View/<slug:slug>', views.ViewTransactionGroup.as_view(), name='ViewTransactionGroup'),
    path('TransactionGroup/Edit/Creditor/<slug:slug>', views.EditTransactionGroupCreditor.as_view(), name='EditTransactionGroupCreditor'),
    path('TransactionGroup/Edit/Debtor/<slug:slug>', views.EditTransactionGroupDebtor.as_view(), name='EditTransactionGroupDebtor'),
    path('TransactionGroup/Edit/Data/<slug:slug>', views.EditTransactionGroupData.as_view(), name='EditTransactionGroupData'),
    path('TransactionGroup/Edit/Action/', views.EditTransactionGroupAction, name='EditTransactionGroupAction'),
    path('TransactionGroup/ToggleApprove/<slug:slug>', views.ToggleApproveTransactionGroup, name='ToggleApproveTransactionGroup'),
    path('TransactionGroup/Delete/<slug:slug>', views.DeleteTransactionGroup.as_view(), name='DeleteTransactionGroup'),

    path('CustomCurrency/Create/', views.CreateCustomCurrency.as_view(), name='CreateCustomCurrency'),
    path('CustomCurrency/List/', views.ListCustomCurrency.as_view(), name='ListCustomCurrency'),
    path('CustomCurrency/Edit/<slug:slug>', views.EditCustomCurrency.as_view(), name='EditCustomCurrency'),
    path('CustomCurrency/Delete/<slug:slug>', views.DeleteCustomCurrency.as_view(), name='DeleteCustomCurrency'),

    path('CustomExpense/Create/', views.CreateCustomExpense.as_view(), name='CreateCustomExpense'),
    path('CustomExpense/List/', views.ListCustomExpense.as_view(), name='ListCustomExpense'),
    path('CustomExpense/Edit/<slug:slug>', views.EditCustomExpense.as_view(), name='EditCustomExpense'),
    path('CustomExpense/Delete/<slug:slug>', views.DeleteCustomExpense.as_view(), name='DeleteCustomExpense'),

    path('FeeTemplate/Create/', views.CreateFeeTemplate.as_view(), name='CreateFeeTemplate'),
    path('FeeTemplate/List/', views.ListFeeTemplate.as_view(), name='ListFeeTemplate'),
    path('FeeTemplate/Edit/<slug:slug>', views.EditFeeTemplate.as_view(), name='EditFeeTemplate'),
    path('FeeTemplate/Delete/<slug:slug>', views.DeleteFeeTemplate.as_view(), name='DeleteFeeTemplate'),

    path('Event/Create/', RedirectView.as_view(url='Setup/'), name='CreateEvent'),
    path('Event/Create/Setup/', views.CreateEventSetup.as_view(), name='CreateEventSetup'),
    path('Event/Create/Data/', views.CreateEventData.as_view(), name='CreateEventData'),
    path('Event/Create/Action/', views.CreateEventAction, name='CreateEventAction'),
    path('Event/View/<slug:slug>', views.ViewEvent.as_view(), name='ViewEvent'),
    path('Event/Edit/Setup/<slug:slug>', views.EditEventSetup.as_view(), name='EditEventSetup'),
    path('Event/Edit/Data/<slug:slug>', views.EditEventData.as_view(), name='EditEventData'),
    path('Event/Edit/Action/', views.EditEventAction, name='EditEventAction'),
    path('Event/ToggleApprove/<slug:slug>', views.ToggleApproveEvent, name='ToggleApproveEvent'),
    path('Event/Delete/<slug:slug>', views.DeleteEvent.as_view(), name='DeleteEvent'),

]
