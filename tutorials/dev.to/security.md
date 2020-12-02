<!--
Title: How to secure an Ubuntu server: the right way
Tags: ubuntu, security, devops, server
 -->

# Introduction

This tutorial will aid you in setting up a secure Ubuntu server from scratch.

Keep in mind that this is not a common tutorial, this is the culmination of all the knowledge I have gathered from managing my own servers for more than three years.

---

## 0. Before we start

### Preface

While this tutorial is focused on Ubuntu 20.04, it can be used for many other versions, like 18.04 and 16.04. As they are very similar.

### Requisites

- An Ubuntu server
- Credentials to your server

_It doesn't matter if your server is hosted on DigitalOcean, Google Cloud Engine or Amazon Web Services, Ubuntu should be the same._

### Requisites info

If you don't have a server you might want to look at the [Useful resources](#useful-resources) step.

---

## Updates

The first and probably most important step is to always keep the system up to date. To do so just open the terminal to update and upgrade our packages via [apt](https://linuxize.com/post/how-to-use-apt-command/).

```sh
sudo apt update           # Update package information
sudo apt full-upgrade -y  # Upgrade packages
sudo apt autoremove -y    # Remove unnecessary packages

# One liner
sudo apt update && sudo apt dist-upgrade -y && sudo apt autoremove -y
```

---

## Automatic updates

Now that our packages are updated, we should install an automated solution to keep our system always up to date.

[This tutorial on Linuxize](https://linuxize.com/post/how-to-set-up-automatic-updates-on-ubuntu-18-04/) will help you install and configure the `unattended-upgrades` package, which is exactly what we need.

---

## New user

Using the default super user `root` is always bad practice, it does everything with the maximum level of permissions, allowing you to break anything; and more critically... _Access to anything on the system_.

Instead, we should use a normal user with super user **privileges**. [This tutorial on DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-20-04-quickstart) will guide you to do so.

---

## SSH credentials

Now that you have a new user with super user privileges, you might want to SSH in your server with it, but might find that you cannot.

This is because the credentials were stored on the user you were using, most likely `root`. Just SSH again with the previous user and copy the credentials with the `rsync` utility package.

Follow the **5th step** of [this tutorial on DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04#if-the-root-account-uses-ssh-key-authentication) to do so.

---

## SSHD

---

## UFW

---

## Fail2Ban

---

## Tips & Tricks

<!-- TODO: PHP info -->
<!-- TODO: database info -->
<!-- TODO: Docker info -->
<!-- TODO: web server info -->

<!-- TODO: recommend Dokku -->

---

## -1. End

### Useful resources

- [How to get a free Google server forever](https://dev.to/phocks/how-to-get-a-free-google-server-forever-1fpf), a perfect test environment for this tutorial.
- [How to get 2x Oracle Cloud servers free forever](https://dev.to/phocks/how-to-get-2x-oracle-cloud-servers-free-forever-4o22), another option for test environments.
- [Create your own Heroku with Dokku on DigitalOcean](https://dev.to/alejandroakbal/create-your-own-heroku-with-dokku-on-digitalocean-14ef), a guide to deploy your applications to your now-secure server.

### Self promotion

If you have found this tutorial useful then you should follow me, I will be posting more interesting content! ♥

- [GitHub](https://github.com/AlejandroAkbal)
- [Twitter](https://twitter.com/AlejandroAkbal)
- [Dev.to](https://dev.to/alejandroakbal)
- [Medium](https://medium.com/@alejandroakbal)
- [LinkedIn](https://www.linkedin.com/in/alejandro-akbal)

Or support me financially

- [GitHub Sponsors](https://github.com/sponsors/AlejandroAkbal)
- [LiberaPay](https://redirect.r34.app/liberapay)
- [PayPal](https://redirect.r34.app/paypal)

### Credit

- DigitalOcean Community
- Linuxize Community
- OSRadar Community