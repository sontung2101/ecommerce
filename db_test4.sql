-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2019 at 10:17 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_test4`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add slide', 6, 'add_slide'),
(22, 'Can change slide', 6, 'change_slide'),
(23, 'Can delete slide', 6, 'delete_slide'),
(24, 'Can view slide', 6, 'view_slide'),
(25, 'Can add cart', 7, 'add_cart'),
(26, 'Can change cart', 7, 'change_cart'),
(27, 'Can delete cart', 7, 'delete_cart'),
(28, 'Can view cart', 7, 'view_cart'),
(29, 'Can add cart item', 8, 'add_cartitem'),
(30, 'Can change cart item', 8, 'change_cartitem'),
(31, 'Can delete cart item', 8, 'delete_cartitem'),
(32, 'Can view cart item', 8, 'view_cartitem'),
(33, 'Can add partner', 9, 'add_partner'),
(34, 'Can change partner', 9, 'change_partner'),
(35, 'Can delete partner', 9, 'delete_partner'),
(36, 'Can view partner', 9, 'view_partner'),
(37, 'Can add type products', 10, 'add_typeproducts'),
(38, 'Can change type products', 10, 'change_typeproducts'),
(39, 'Can delete type products', 10, 'delete_typeproducts'),
(40, 'Can view type products', 10, 'view_typeproducts'),
(41, 'Can add products', 11, 'add_products'),
(42, 'Can change products', 11, 'change_products'),
(43, 'Can delete products', 11, 'delete_products'),
(44, 'Can view products', 11, 'view_products'),
(45, 'Can add user', 12, 'add_customeruser'),
(46, 'Can change user', 12, 'change_customeruser'),
(47, 'Can delete user', 12, 'delete_customeruser'),
(48, 'Can view user', 12, 'view_customeruser');

-- --------------------------------------------------------

--
-- Table structure for table `cart_cart`
--

CREATE TABLE `cart_cart` (
  `id` int(11) NOT NULL,
  `total` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `Partner_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `cart_cartitem`
--

CREATE TABLE `cart_cartitem` (
  `id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_price` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `Cart_id` int(11) NOT NULL,
  `Products_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(7, 'cart', 'cart'),
(8, 'cart', 'cartitem'),
(4, 'contenttypes', 'contenttype'),
(6, 'home', 'slide'),
(9, 'order', 'partner'),
(11, 'product', 'products'),
(10, 'product', 'typeproducts'),
(5, 'sessions', 'session'),
(12, 'user', 'customeruser');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-12-01 10:23:25.931963'),
(2, 'contenttypes', '0002_remove_content_type_name', '2019-12-01 10:23:26.029705'),
(3, 'auth', '0001_initial', '2019-12-01 10:23:26.202240'),
(4, 'auth', '0002_alter_permission_name_max_length', '2019-12-01 10:23:26.605163'),
(5, 'auth', '0003_alter_user_email_max_length', '2019-12-01 10:23:26.611148'),
(6, 'auth', '0004_alter_user_username_opts', '2019-12-01 10:23:26.617131'),
(7, 'auth', '0005_alter_user_last_login_null', '2019-12-01 10:23:26.623116'),
(8, 'auth', '0006_require_contenttypes_0002', '2019-12-01 10:23:26.626108'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2019-12-01 10:23:26.632116'),
(10, 'auth', '0008_alter_user_username_max_length', '2019-12-01 10:23:26.638075'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2019-12-01 10:23:26.644059'),
(12, 'auth', '0010_alter_group_name_max_length', '2019-12-01 10:23:26.726085'),
(13, 'auth', '0011_update_proxy_permissions', '2019-12-01 10:23:26.733066'),
(14, 'user', '0001_initial', '2019-12-01 10:23:26.858904'),
(15, 'admin', '0001_initial', '2019-12-01 10:23:27.274097'),
(16, 'admin', '0002_logentry_remove_auto_add', '2019-12-01 10:23:27.438059'),
(17, 'admin', '0003_logentry_add_action_flag_choices', '2019-12-01 10:23:27.446029'),
(18, 'product', '0001_initial', '2019-12-01 10:23:27.646711'),
(19, 'order', '0001_initial', '2019-12-01 10:23:27.787363'),
(20, 'cart', '0001_initial', '2019-12-01 10:23:27.877373'),
(21, 'cart', '0002_remove_cart_date_order', '2019-12-01 10:23:28.079467'),
(22, 'home', '0001_initial', '2019-12-01 10:23:28.115339'),
(23, 'order', '0002_auto_20191129_1632', '2019-12-01 10:23:28.121348'),
(24, 'order', '0003_auto_20191129_1642', '2019-12-01 10:23:28.126342'),
(25, 'order', '0004_auto_20191201_1723', '2019-12-01 10:23:28.131296'),
(26, 'sessions', '0001_initial', '2019-12-01 10:23:28.185185'),
(27, 'user', '0002_remove_customeruser_note', '2019-12-01 10:23:28.220092');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4si939qxm29zupccrbs41f8022vlq4ua', 'MDA5MDRhMmM0NmUxNDZmZTUxYzhmZWI4YTNlODQxMzllNjA3ZTk5NDp7ImNhcnQiOnsiMTAiOnsibmFtZSI6IkRyZXNzNCIsInByaWNlIjoxMDAwMDAwLCJpbWciOiJkcmVzczRhLmpwZyIsIm51bSI6IjEifX19', '2019-12-15 10:28:59.515108');

-- --------------------------------------------------------

--
-- Table structure for table `home_slide`
--

CREATE TABLE `home_slide` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `main` varchar(100) DEFAULT NULL,
  `link` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `home_slide`
--

INSERT INTO `home_slide` (`id`, `title`, `main`, `link`, `image`) VALUES
(1, 'Hello World JD 2019', 'Python', '', 'master-slide-02.jpg'),
(2, 'Hello World JD 2019', 'Just Django', '', 'master-slide-07.jpg'),
(3, 'Hello World JD 2019', 'Hello World', '', 'master-slide-04.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `order_partner`
--

CREATE TABLE `order_partner` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `note` varchar(255) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `customeruser_id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `product_products`
--

CREATE TABLE `product_products` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `unit_price` int(11) NOT NULL,
  `promotion_price` int(11) NOT NULL,
  `inventory` int(11) NOT NULL,
  `unit` varchar(100) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `new` tinyint(1) NOT NULL,
  `image` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `TypeProducts_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_products`
--

INSERT INTO `product_products` (`id`, `name`, `description`, `unit_price`, `promotion_price`, `inventory`, `unit`, `active`, `new`, `image`, `created_at`, `updated_at`, `TypeProducts_id`) VALUES
(1, 'Dress1', 'main', 500000, 0, 0, 'chiếc', 0, 0, 'dress1.jpg', '2019-11-12 10:54:12.000000', '2019-11-12 10:54:16.000000', 6),
(3, 'Dress2', 'main', 550000, 350000, 0, 'chiếc', 0, 1, 'dress2.jpg', '2019-11-12 10:54:18.000000', '2019-11-12 10:54:21.000000', 6),
(8, 'Dress3', 'main', 700000, 0, 0, 'chiếc', 0, 0, 'dress3a.jpg', '2019-11-12 10:54:23.000000', '2019-11-12 10:54:26.000000', 6),
(10, 'Dress4', 'main', 1000000, 0, 0, 'chiếc', 0, 0, 'dress4a.jpg', '2019-11-12 11:01:49.000000', '2019-11-12 11:01:52.000000', 6),
(11, 'Dress5', 'main', 2500000, 0, 0, 'chiếc', 0, 0, 'dress5a.jpg', '2019-11-12 11:02:37.000000', '2019-11-12 11:02:43.000000', 6),
(12, 'Dress6', 'main', 200000, 0, 0, 'chiếc', 0, 0, 'dress6a.jpg', '2019-11-12 11:03:38.000000', '2019-11-12 11:03:40.000000', 6),
(13, 'Dress7', 'main', 535000, 500000, 0, 'chiếc', 0, 1, 'dress7a.jpg', '2019-11-12 11:04:37.000000', '2019-11-12 11:04:40.000000', 6),
(14, 'Dress8', 'main', 1250000, 0, 0, 'chiếc', 0, 1, 'dress8a.jpg', '2019-11-12 11:05:27.000000', '2019-11-12 11:05:30.000000', 6),
(20, 'Dress9', 'main', 200000, 0, 0, 'chiếc', 0, 1, 'dress10a.jpg', '2019-11-12 12:14:34.000000', '2019-11-12 12:14:37.000000', 6),
(21, 'Dress10', 'main', 100000, 25000, 0, 'chiếc', 0, 0, 'dress9a.jpg', '2019-11-12 13:50:54.000000', '2019-11-12 13:50:57.000000', 6),
(22, 'Jacket1', 'main', 10000, 25000, 0, 'chiếc', 0, 1, 'jacket1a.jpg', '2019-11-12 14:32:48.000000', '2019-11-12 14:32:51.000000', 7),
(24, 'Jacket2', 'main', 700000, 0, 0, 'chiếc', 0, 0, 'jacket2a.jpg', '2019-11-12 14:34:08.000000', '2019-11-12 14:34:12.000000', 7),
(26, 'jacket3', 'main', 1234560, 100000, 0, 'chiếc', 0, 0, 'jacket3a.jpg', '2019-11-12 14:35:34.000000', '2019-11-12 14:35:36.000000', 7),
(28, 'Jacket4', 'main', 1000000, 500000, 0, 'chiếc', 0, 1, 'jacket4a.jpg', '2019-11-12 14:41:34.000000', '2019-11-12 14:41:37.000000', 7),
(29, 'Jacket5', 'main', 1300000, 1250000, 0, 'chiếc', 0, 1, 'jacket5a.jpg', '2019-11-12 14:42:25.000000', '2019-11-12 14:42:28.000000', 7);

-- --------------------------------------------------------

--
-- Table structure for table `product_typeproducts`
--

CREATE TABLE `product_typeproducts` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(255) NOT NULL,
  `type_parent` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_typeproducts`
--

INSERT INTO `product_typeproducts` (`id`, `name`, `description`, `image`, `type_parent`, `active`, `created_at`, `updated_at`) VALUES
(1, 'All', 'tất cả', '', 1, 127, '2019-11-08 15:17:53.000000', '0000-00-00 00:00:00.000000'),
(2, 'Women', 'nữ', '', 0, 127, '2019-11-08 15:18:43.000000', '0000-00-00 00:00:00.000000'),
(3, 'Men', 'nam', '', 0, 127, '2019-11-08 15:33:54.000000', '0000-00-00 00:00:00.000000'),
(4, 'Kids', 'trẻ em', '', 0, 127, '2019-11-08 15:33:51.000000', '0000-00-00 00:00:00.000000'),
(5, 'Accesories', 'Phụ kiện', '', 0, 127, '2019-11-08 15:33:49.000000', '0000-00-00 00:00:00.000000'),
(6, 'Dresses', 'váy', '', 2, 127, '2019-11-08 15:33:46.000000', '0000-00-00 00:00:00.000000'),
(7, 'Jacket', 'Áo khoác', '', 2, 127, '2019-11-08 15:33:44.000000', '0000-00-00 00:00:00.000000'),
(8, 'Pant', 'quần', '', 2, 127, '2019-11-08 15:33:41.000000', '0000-00-00 00:00:00.000000'),
(9, 'T-Shirt', 'áo sơ mi', '', 3, 127, '2019-11-08 15:34:46.000000', '0000-00-00 00:00:00.000000'),
(10, 'Jean', 'quần bò', '', 3, 127, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(11, 'Shirt', 'áo trẻ em', '', 4, 127, '2019-11-08 15:46:41.000000', '0000-00-00 00:00:00.000000'),
(12, 'Pant', 'quần trẻ em', '', 4, 127, '2019-11-08 15:46:46.000000', '0000-00-00 00:00:00.000000'),
(13, 'Watches', 'đồng hồ', '', 5, 127, '2019-11-08 15:47:54.000000', '0000-00-00 00:00:00.000000'),
(14, 'Bags', 'Cặp', '', 5, 127, '2019-11-08 15:48:14.000000', '0000-00-00 00:00:00.000000'),
(15, 'Sunglasses', 'Kính', '', 5, 127, '2019-11-08 15:48:54.000000', '0000-00-00 00:00:00.000000'),
(16, 'Footerwear', 'giày', '', 5, 127, '2019-11-08 15:50:35.000000', '0000-00-00 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `user_customeruser`
--

CREATE TABLE `user_customeruser` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone_number` int(11) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user_customeruser_groups`
--

CREATE TABLE `user_customeruser_groups` (
  `id` int(11) NOT NULL,
  `customeruser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user_customeruser_user_permissions`
--

CREATE TABLE `user_customeruser_user_permissions` (
  `id` int(11) NOT NULL,
  `customeruser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `cart_cart`
--
ALTER TABLE `cart_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cart_cart_Partner_id_3c0372e5_fk_order_partner_id` (`Partner_id`);

--
-- Indexes for table `cart_cartitem`
--
ALTER TABLE `cart_cartitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cart_cartitem_Cart_id_d6c89d51_fk_cart_cart_id` (`Cart_id`),
  ADD KEY `cart_cartitem_Products_id_ff0c1c99_fk_product_products_id` (`Products_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_user_customeruser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `home_slide`
--
ALTER TABLE `home_slide`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order_partner`
--
ALTER TABLE `order_partner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product_products`
--
ALTER TABLE `product_products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_products_TypeProducts_id_2cef5c8e_fk_product_t` (`TypeProducts_id`);

--
-- Indexes for table `product_typeproducts`
--
ALTER TABLE `product_typeproducts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_customeruser`
--
ALTER TABLE `user_customeruser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `user_customeruser_groups`
--
ALTER TABLE `user_customeruser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_customeruser_groups_customeruser_id_group_id_3d678a1c_uniq` (`customeruser_id`,`group_id`),
  ADD KEY `user_customeruser_groups_group_id_d0edfea3_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `user_customeruser_user_permissions`
--
ALTER TABLE `user_customeruser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_customeruser_user_p_customeruser_id_permissi_0ae3e6b5_uniq` (`customeruser_id`,`permission_id`),
  ADD KEY `user_customeruser_us_permission_id_2f237c7d_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `cart_cart`
--
ALTER TABLE `cart_cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cart_cartitem`
--
ALTER TABLE `cart_cartitem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `home_slide`
--
ALTER TABLE `home_slide`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `order_partner`
--
ALTER TABLE `order_partner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `product_products`
--
ALTER TABLE `product_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `product_typeproducts`
--
ALTER TABLE `product_typeproducts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `user_customeruser`
--
ALTER TABLE `user_customeruser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_customeruser_groups`
--
ALTER TABLE `user_customeruser_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_customeruser_user_permissions`
--
ALTER TABLE `user_customeruser_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `cart_cart`
--
ALTER TABLE `cart_cart`
  ADD CONSTRAINT `cart_cart_Partner_id_3c0372e5_fk_order_partner_id` FOREIGN KEY (`Partner_id`) REFERENCES `order_partner` (`id`);

--
-- Constraints for table `cart_cartitem`
--
ALTER TABLE `cart_cartitem`
  ADD CONSTRAINT `cart_cartitem_Cart_id_d6c89d51_fk_cart_cart_id` FOREIGN KEY (`Cart_id`) REFERENCES `cart_cart` (`id`),
  ADD CONSTRAINT `cart_cartitem_Products_id_ff0c1c99_fk_product_products_id` FOREIGN KEY (`Products_id`) REFERENCES `product_products` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_customeruser_id` FOREIGN KEY (`user_id`) REFERENCES `user_customeruser` (`id`);

--
-- Constraints for table `product_products`
--
ALTER TABLE `product_products`
  ADD CONSTRAINT `product_products_TypeProducts_id_2cef5c8e_fk_product_t` FOREIGN KEY (`TypeProducts_id`) REFERENCES `product_typeproducts` (`id`);

--
-- Constraints for table `user_customeruser_groups`
--
ALTER TABLE `user_customeruser_groups`
  ADD CONSTRAINT `user_customeruser_gr_customeruser_id_91d892ca_fk_user_cust` FOREIGN KEY (`customeruser_id`) REFERENCES `user_customeruser` (`id`),
  ADD CONSTRAINT `user_customeruser_groups_group_id_d0edfea3_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `user_customeruser_user_permissions`
--
ALTER TABLE `user_customeruser_user_permissions`
  ADD CONSTRAINT `user_customeruser_us_customeruser_id_a1543949_fk_user_cust` FOREIGN KEY (`customeruser_id`) REFERENCES `user_customeruser` (`id`),
  ADD CONSTRAINT `user_customeruser_us_permission_id_2f237c7d_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
