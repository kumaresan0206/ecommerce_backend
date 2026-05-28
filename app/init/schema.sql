-- init/schema.sql


-- =========================
-- USERS TABLE
-- =========================

CREATE TABLE IF NOT EXISTS users (

    id SERIAL PRIMARY KEY,

    name VARCHAR(255) NOT NULL,

    email VARCHAR(255) UNIQUE NOT NULL,

    password TEXT NOT NULL,

    role VARCHAR(50) DEFAULT 'customer',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- =========================
-- PRODUCTS TABLE
-- =========================

CREATE TABLE IF NOT EXISTS products (

    id SERIAL PRIMARY KEY,

    name VARCHAR(255) NOT NULL,

    description TEXT,

    price NUMERIC(10, 2) NOT NULL,

    stock INTEGER DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- =========================
-- ORDERS TABLE
-- =========================

CREATE TABLE IF NOT EXISTS orders (

    id SERIAL PRIMARY KEY,

    user_id INTEGER NOT NULL,

    product_id INTEGER NOT NULL,

    quantity INTEGER NOT NULL,

    address TEXT NOT NULL,

    CONSTRAINT fk_order_user
        FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_order_product
        FOREIGN KEY(product_id)
        REFERENCES products(id)
        ON DELETE CASCADE
);



-- =========================
-- CART TABLE
-- =========================

CREATE TABLE IF NOT EXISTS cart (

    id SERIAL PRIMARY KEY,

    user_id INTEGER NOT NULL,

    product_id INTEGER NOT NULL,

    quantity INTEGER NOT NULL DEFAULT 1,

    CONSTRAINT fk_cart_user
        FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_cart_product
        FOREIGN KEY(product_id)
        REFERENCES products(id)
        ON DELETE CASCADE
);



-- =========================
-- INDEXES
-- =========================

CREATE INDEX IF NOT EXISTS idx_users_email
ON users(email);


CREATE INDEX IF NOT EXISTS idx_products_name
ON products(name);


CREATE INDEX IF NOT EXISTS idx_orders_user_id
ON orders(user_id);


CREATE INDEX IF NOT EXISTS idx_cart_user_id
ON cart(user_id);