// Copyright (c) 2025, Santha Ashwin and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airline', {
       refresh(frm) {
         const your_link = frm.doc.route;
         frm.add_web_link(your_link, "View Airline website");
       }
     });

     