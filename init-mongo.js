db.createUser(
    {
        user: "trading_user",
        pwd: "trading_pass",
        roles: [
            {
                role: "readWrite",
                db: "mongo"
            }
        ]
    }
);
db.createCollection("trading");