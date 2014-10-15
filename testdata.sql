INSERT INTO reservations_company (id, name, street_address, postcode, city, contact_person, phone, business_id, iban, location_vat)
VALUES
(1, 'Feel Like Oy', 'Loimitie 11 A 1', '01260', 'Vantaa', 'Mikko Vikman', '046 568 7281', '2622082-9', 'FI23 8146 9710 0802 26', 10);
	

INSERT INTO reservations_customer (id, first_name, last_name, email, street_address, postcode, city, phone, discount)
VALUES
(1, 'John', 'Doe', 'john.doe@email.com', 'Somestreet 123', '01370', 'Vantaa', '+123456789', 0),
(2, 'Jane', 'Doe', 'jane.doe@email.com', 'Somestreet 123', '01370', 'Vantaa', '+123456788', 0),
(3, 'John', 'Smith', 'john.smith@email.com', 'Otherstreet 456', '01371', 'Elsewhere', '+9876543321', 0),
(4, 'Jane', 'Smith', 'jane.smith@email.com', 'Otherstreet 456', '01371', 'Elsewhere', '+9876543322', 0);


INSERT INTO reservations_coach (id, first_name, last_name, phone)
VALUES
(1, 'Mikko', 'Vikman', '046 568 7281'),
(2, 'Emma', 'Sjölund', '046 568 7281');


INSERT INTO reservations_product (id, name, price, vat)
VALUES
(1, 'Personal training', 99.99, 23),
(2, 'Group training', 199.99, 23);


INSERT INTO reservations_reservation (id, start_time, end_time, customer_id, coach_id, product_id, location, location_price, participants, amount)
VALUES
(1, '2014-10-16 10:00', '2014-10-16 12:00', 1, 1, 1, 'Some sports hall', 49.99, 1, 149.99),
(2, '2014-10-16 12:00', '2014-10-16 14:00', 3, 1, 1, 'Some sports hall', 49.99, 1, 149.99),
(3, '2014-10-17 14:00', '2014-10-17 16:00', 1, 2, 1, 'Some sports hall', 49.99, 1, 149.99),
(4, '2014-10-17 16:00', '2014-10-17 18:00', 2, 1, 2, 'Some sports hall', 49.99, 4, 249.99),
(5, '2014-10-18 10:00', '2014-10-18 12:00', 1, 2, 1, 'Some sports hall', 49.99, 1, 149.99),
(6, '2014-10-18 14:00', '2014-10-18 16:00', 4, 1, 1, 'Some sports hall', 49.99, 1, 149.99);


INSERT INTO reservations_invoice (id, date, reservation_id, company_id)
VALUES
(1, '2014-10-16', 1, 1),
(2, '2014-10-16', 2, 1),
(3, '2014-10-17', 3, 1),
(4, '2014-10-17', 4, 1),
(5, '2014-10-18', 5, 1),
(6, '2014-10-18', 6, 1);
