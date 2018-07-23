# Authentication and User Basics

The default Authenticator uses [PAM][] to authenticate system users with
their username and password. With the default Authenticator, any user
with an account and password on the system will be allowed to login.

## Create a whitelist of users

You can restrict which users are allowed to login with a whitelist,
`Authenticator.whitelist`:


```python
c.Authenticator.whitelist = {'mal', 'zoe', 'inara', 'kaylee'}
```

Users in the whitelist are added to the Hub database when the Hub is
started.

## Configure admins (`admin_users`)

Admin users of JupyterHub, `admin_users`, can add and remove users from
the user `whitelist`. `admin_users` can take actions on other users'
behalf, such as stopping and restarting their servers.

A set of initial admin users, `admin_users` can configured be as follows:

```python
c.Authenticator.admin_users = {'mal', 'zoe'}
```
Users in the admin list are automatically added to the user `whitelist`,
if they are not already present.

## Give admin access to other users' notebook servers (`admin_access`)

Since the default `JupyterHub.admin_access` setting is False, the admins
do not have permission to log in to the single user notebook servers
owned by *other users*. If `JupyterHub.admin_access` is set to True,
then admins have permission to log in *as other users* on their
respective machines, for debugging. **As a courtesy, you should make
sure your users know if admin_access is enabled.**

## Add or remove users from the Hub

Users can be added to and removed from the Hub via either the admin
panel or the REST API. When a user is **added**, the user will be
automatically added to the whitelist and database. Restarting the Hub
will not require manually updating the whitelist in your config file,
as the users will be loaded from the database.

After starting the Hub once, it is not sufficient to **remove** a user
from the whitelist in your config file. You must also remove the user
from the Hub's database, either by deleting the user from JupyterHub's
admin page, or you can clear the `jupyterhub.sqlite` database and start
fresh.

## Use LocalAuthenticator to create system users

The `LocalAuthenticator` is a special kind of authenticator that has
the ability to manage users on the local system. When you try to add a
new user to the Hub, a `LocalAuthenticator` will check if the user
already exists. If you set the configuration value, `create_system_users`,
to `True` in the configuration file, the `LocalAuthenticator` has
the privileges to add users to the system. The setting in the config
file is:

```python
c.LocalAuthenticator.create_system_users = True
```

Adding a user to the Hub that doesn't already exist on the system will
result in the Hub creating that user via the system `adduser` command
line tool. This option is typically used on hosted deployments of
JupyterHub, to avoid the need to manually create all your users before
launching the service. This approach is not recommended when running
JupyterHub in situations where JupyterHub users map directly onto the
system's UNIX users.

## Use OAuthenticator to support OAuth with popular service providers

JupyterHub's [OAuthenticator][] currently supports the following
popular services:

- Auth0
- Bitbucket
- CILogon
- GitHub
- GitLab
- Globus
- Google
- MediaWiki
- Okpy
- OpenShift

A generic implementation, which you can use for OAuth authentication
with any provider, is also available.

[PAM]: https://en.wikipedia.org/wiki/Pluggable_authentication_module
[OAuthenticator]: https://github.com/jupyterhub/oauthenticator