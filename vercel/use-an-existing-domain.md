# Use an existing domain

### Using CLI?

Use this snippet to add a domain that you own to a Vercel project:

terminal

```
vercel domains add [domain] [project]
```

Already have a domain you love? Seamlessly integrate it with Vercel to leverage the platform's powerful features and infrastructure. Whether you're migrating an existing project or want to maintain your established online presence, you can use the steps below to add your custom domain.

1. ### [Go to your project's domains settings](#go-to-your-project's-domains-settings)

    Select your project and select the Settings tab. Then, select the Domains menu item or click on this [link](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdomains&title=Go+to+Domains) and select your project

2. ### [Add your existing domain to your project](#add-your-existing-domain-to-your-project)

    From the Domains page, enter the domain you wish to add to the project.

    If you add an apex domain (e.g. `example.com`) to the project, Vercel will prompt you to add the `www`subdomain prefix, the apex domain, and [some basic redirection options](/docs/domains/deploying-and-redirecting).

    For more information on which redirect option to choose, see [Redirecting `www` domains](/docs/domains/deploying-and-redirecting#redirecting-www-domains).

3. ### [Configure your DNS records](#configure-your-dns-records)

    Configure the DNS records of your domain with your registrar so it can be used with your Project. The dashboard will automatically display different methods for configuring it:

    * If the domain is in use by another Vercel account, you will need to [verify access to the domain](/docs/domains/add-a-domain#verify-domain-access), with a TXT record
    * If you're using an [Apex domain](/docs/domains/add-a-domain#apex-domains) (e.g. example.com), you will need to configure it with an A record
    * If you're using a [Subdomain](/docs/domains/add-a-domain#subdomains) (e.g. docs.example.com), you will need to configure it with a CNAME record

    Both apex domains and subdomains can also be configured using the [Nameservers](/docs/domains/add-a-domain#vercel-nameservers) method. Wildcard domains must use the nameservers method for verification. For more information see [Add a custom domain](/docs/domains/add-a-domain).

## [Next steps](#next-steps)

Next, learn how to take advantage of Vercel's collaboration features as part of your developer workflow:

[

Use Vercel in your developer workflow

](/docs/getting-started-with-vercel/collaborate)
