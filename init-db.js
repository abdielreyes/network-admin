db = db.getSiblingDB("netadmin_db");
db.user_tb.drop();

db.user_tb.insertMany([
  {
    username: "root",
    password: "root",
    email: "root@root.com",
  },
  {
    username: "abdiel",
    password: "abdiel123",
    email: "abykings1@gmail.com",
  },
  {
    username: "marigaac1d",
    password: "mari123",
    email: "marielessgama@hotmail.com",
  },
]);
