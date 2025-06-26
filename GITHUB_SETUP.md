# 📦 GitHub Container Registry Setup

This guide helps you set up GitHub Container Registry (GHCR) for your entry control system.

## 🔑 Step 1: Create Personal Access Token

1. **Go to GitHub Token Settings**: https://github.com/settings/tokens
2. **Click "Generate new token"** → "Generate new token (classic)"
3. **Configure the token**:
   - **Note**: `Entry Control System - Container Registry`
   - **Expiration**: Choose your preferred duration
   - **Scopes**: Check the following boxes:
     - ✅ `write:packages` (Upload packages to GitHub Package Registry)
     - ✅ `read:packages` (Download packages from GitHub Package Registry)
     - ✅ `delete:packages` (Delete packages from GitHub Package Registry) - optional

4. **Generate token** and **copy it immediately** (you won't see it again!)

## 🚀 Step 2: Run the Setup Script

```bash
# Replace 'your-github-username' with your actual GitHub username
./deploy-setup.sh your-github-username
```

**When prompted for credentials:**
- **Username**: Your GitHub username (e.g., `johndoe`)
- **Password**: Your Personal Access Token (NOT your GitHub password!)

## 📦 Step 3: Verify Your Packages

After the script completes, you can view your packages at:
```
https://github.com/YOUR_USERNAME?tab=packages
```

You should see:
- `entry-control-backend` 
- `entry-control-frontend`

## 🔒 Package Visibility

By default, packages are **private**. To make them public (so others can pull without authentication):

1. Go to your package page
2. Click **"Package settings"** (bottom right)
3. Scroll to **"Danger Zone"**
4. Click **"Change visibility"**
5. Select **"Public"**
6. Type the package name to confirm

## 🎯 Benefits of GitHub Container Registry

- ✅ **Free for public repositories**
- ✅ **Integrated with your GitHub repo**
- ✅ **Better than Docker Hub for open source**
- ✅ **Automatic security scanning**
- ✅ **Fine-grained access control**
- ✅ **Unlimited bandwidth for public packages**

## 🐛 Troubleshooting

### Login Issues
```bash
# If login fails, try:
podman logout ghcr.io
podman login ghcr.io
```

### Permission Denied
- Make sure your token has `write:packages` scope
- Check if you're using the token (not password) for login

### Package Not Found
- Verify the package name matches your GitHub username
- Check if the package is public if others are trying to pull

### Rate Limits
- GHCR has generous rate limits for authenticated users
- Public packages have unlimited bandwidth

## 💡 Pro Tips

1. **Keep your token secure** - treat it like a password
2. **Use repository secrets** for CI/CD automation
3. **Make packages public** for open source projects
4. **Use semantic versioning** for your tags (v1.0.0, v1.1.0, etc.)

## 📚 Additional Resources

- [GitHub Container Registry Documentation](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- [Managing Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
