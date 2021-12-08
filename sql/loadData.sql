INSERT INTO Message(id, sender, contents) VALUES
(1, 'JD', 'Hey, hows it going?'),
(2, 'WS', 'Hey, not too bad how about yourself'),
(3, 'JD', 'Cant complain. Are you planning to do anything for Christmas'),
(4, 'JD', 'Im planning a ski trip with some friends. Wanna tag along'),
(5, 'WS', 'Sure! Let me know the details. Thanks :)');


INSERT INTO Room(id, msgId) VALUES
(0, 1),
(0, 2),
(0, 3),
(0, 4),
(0, 5);