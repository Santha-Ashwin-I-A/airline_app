// Copyright (c) 2025, Santha Ashwin and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });



frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button(__('Action'), function() {
            let d = new frappe.ui.Dialog({
                title: 'Enter Seat No',
                fields: [
                {
                    label: 'Seat',
                    fieldname: 'seat_up',
                    fieldtype: 'Data'
                }
                ],
                size: 'small', // small, large, extra-large 
                primary_action_label: 'Submit',
                primary_action(values) {
                    a=values;
                    console.log("A=",a)
                    if(a!=null){
                        frm.set_value("seat",a.seat_up)
                        frm.save()
                    }
                    d.hide();
                }
            });
            d.show()
           
            
        });
        
	},
});
