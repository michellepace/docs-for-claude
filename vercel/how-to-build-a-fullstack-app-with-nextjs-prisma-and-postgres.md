# How to Build a Fullstack App with Next.js, Prisma, and Postgres

Create a fullstack application with Next.js, Prisma, Postgres, and deploy to Vercel.

[![Avatar for leerob](https://vercel.com/api/www/avatar?s=40&u=leerob)Lee RobinsonVP of Developer Experience](https://x.com/leerob)

[Guides](https://vercel.com/guides)/Databases & CMS

14 min read Copy page

Last updatedSeptember 8, 2025

[Prisma](https://prisma.io/) is a next-generation ORM that can be used to access a database in Node.js and TypeScript applications. In this guide, you'll learn how to implement a sample fullstack blogging application using the following technologies:

- [Next.js](https://nextjs.org/) as the React framework
- [Next.js API Routes](https://nextjs.org/docs/api-routes/introduction) for server-side API routes as the backend
- [Prisma](https://prisma.io/) as the ORM for migrations and database access
- [Postgres](https://vercel.com/storage/postgres) as the database
- [NextAuth.js](https://next-auth.js.org/) for authentication via GitHub (OAuth)
- [TypeScript](https://www.typescriptlang.org/) as the programming language
- [Vercel](http://vercel.com/) for deployment

You'll take advantage of the flexible rendering capabilities of Next.js and at the end, you will deploy the app to Vercel.

## [Prerequisites](https://vercel.com/guides/nextjs-prisma-postgres\#prerequisites)

To successfully finish this guide, you'll need:

- Node.js
- A Vercel Account (to set up a free Postgres database and deploy the app)
- A GitHub Account (to create an OAuth app)

## [Step 1: Set up your Next.js starter project](https://vercel.com/guides/nextjs-prisma-postgres\#step-1:-set-up-your-next.js-starter-project)

Navigate into a directory of your choice and run the following command in your terminal to set up a new Next.js project with the pages router:

```bash
1npx create-next-app --example https://github.com/prisma/blogr-nextjs-prisma/tree/main blogr-nextjs-prisma
```

Create and download the starter project from the repo into a new folder.

You can now navigate into the directory and launch the app:

```bash
1cd blogr-nextjs-prisma && npm run dev
```

Start the Next.js application at <https://localhost:3000>.

Here's what it looks like at the moment:

![Current state of the application.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2urWoZq7yHkEhi93PPJXD4%2Fec4c90b45389261b215a499f24caaeb4%2F1.png&w=3840&q=75)

Current state of the application.

The app currently displays hardcoded data that's returned from `getStaticProps` in the `index.tsx` file. Over the course of the next few sections, you'll change this so that the data is returned from an actual database.

## [Step 2: Set up your Postgres database](https://vercel.com/guides/nextjs-prisma-postgres\#step-2:-set-up-your-postgres-database)

For the purpose of this guide, we'll use a free Postgres database hosted on Vercel. First, push the repo you cloned in Step 1 to our own GitHub and deploy it to Vercel to create a Vercel project.

Once you have a Vercel project, select the **Storage** tab, then select the **Connect Database** button. Under the **Create New** tab, pick your favorite Postgres provider.

Our empty database is created in the region specified. Because you created the Postgres database in a project, we automatically created and added the following environment variables to the project for you.

After running `npm i -g vercel@latest` to install the Vercel CLI, pull down the latest environment variables to get your local project working with the Postgres database.

```bash
1vercel env pull .env
```

Pull down all the required environment variables locally from the Vercel project

We now have a fully functioning Postgres database and have all the environment variables to run it locally and on Vercel.

## [Step 3: Setup Prisma and create the database schema](https://vercel.com/guides/nextjs-prisma-postgres\#step-3:-setup-prisma-and-create-the-database-schema)

Next, you will set up Prisma and connect it to your PostgreSQL database. Start by installing the Prisma CLI via npm:

```bash
1npm install prisma --save-dev
```

Install the Prisma CLI.

You'll now create the tables in your database using the Prisma CLI.

To do this, create a prisma folder and add a file called `schema.prisma,`your main Prisma configuration file that will contain your database schema.

Add the following model definitions to your `schema.prisma` so that it looks like this:

```text
1// schema.prisma

2

3generator client {

4  provider = "prisma-client-js"

5}

6

7datasource db {

8  provider = "postgresql"

9  url = env("POSTGRES_PRISMA_URL") // uses connection pooling

10  directUrl = env("POSTGRES_URL_NON_POOLING") // uses a direct connection

11}

12

13model Post {

14  id        String     @default(cuid()) @id

15  title     String

16  content   String?

17  published Boolean @default(false)

18  author    User?   @relation(fields: [authorId], references: [id])

19  authorId  String?

20}

21

22model User {

23  id            String       @default(cuid()) @id

24  name          String?

25  email         String?   @unique

26  createdAt     DateTime  @default(now()) @map(name: "created_at")

27  updatedAt     DateTime  @updatedAt @map(name: "updated_at")

28  posts         Post[]

29  @@map(name: "users")

30}
```

The Prisma schema.

**Note:** You're occasionally using [\`@map\`](https://www.prisma.io/docs/reference/api-reference/prisma-schema-reference/#map) and [\`@@map\`](https://www.prisma.io/docs/reference/api-reference/prisma-schema-reference/#map-1) to map some field and model names to different column and table names in the underlying database. This is because NextAuth.js has some special [requirements](https://authjs.dev/reference/adapter/prisma#naming-conventions) for calling things in your database a certain way.

This Prisma schema defines two _models_, each of which will map to a _table_ in the underlying database: `User` and `Post`. Notice that there's also a relation (one-to-many) between the two models, via the `author` field on `Post` and the `posts` field on `User`.

To actually create the tables in your database, you now can use the following command of the Prisma CLI:

```bash
1npx prisma db push
```

Create the tables in your database based on your Prisma schema.

You should see the following output:

```text
1Environment variables loaded from /Users/nikolasburk/Desktop/nextjs-guide/blogr-starter/.env.development.local

2Prisma schema loaded from prisma/schema.prisma

3

4🚀  Your database is now in sync with your schema. Done in 2.10s
```

Output from pushing your Prisma schema to your database.

Congratulations, the tables have been created! Go ahead and add some initial dummy data using Prisma Studio. Run the following command:

```bash
1npx prisma studio
```

Open Prisma Studio, a GUI for modifying your database.

Use Prisma Studio's interface to create a new `User` and `Post` record and connect them via their relation fields.

![Create a new `User` record](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F4Xv0gxUZulUcEbkx44meID%2F35c49dbd5d8e10e3796e920e1270df7f%2F2.png&w=1920&q=75)

Create a new \`User\` record

![Create a new `Post` record and connect it to the `User` record](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F4gg9hkQjCaRfZuGPNrD7Ao%2Ff35ec469a65f168970d190f46dd20872%2F3.png&w=1920&q=75)

Create a new \`Post\` record and connect it to the \`User\` record

## [Step 4. Install and generate Prisma Client](https://vercel.com/guides/nextjs-prisma-postgres\#step-4.-install-and-generate-prisma-client)

Before you can access your database from Next.js using Prisma, you first need to install Prisma Client in your app. You can install it via npm as follows:

```bash
1npm install @prisma/client
```

Install the Prisma Client package.

Because Prisma Client is _tailored_ to your own schema, you need to update it every time your Prisma schema file is changing by running the following command:

```bash
1npx prisma generate
```

Regenerate your Prisma Schema.

You'll use a single `PrismaClient` instance that you can import into any file where it's needed. The instance will be created in a `prisma.ts` file inside the `lib/` directory. Go ahead and create the missing directory and file:

```bash
1mkdir lib && touch lib/prisma.ts
```

Create a new folder for the Prisma library.

Now, add the following code to this file:

lib/prisma.ts

```javascript
1import { PrismaClient } from '@prisma/client';

2

3let prisma: PrismaClient;

4

5if (process.env.NODE_ENV === 'production') {

6  prisma = new PrismaClient();

7} else {

8  if (!global.prisma) {

9    global.prisma = new PrismaClient();

10  }

11  prisma = global.prisma;

12}

13

14export default prisma;
```

Create a connection to your Prisma Client.

Now, whenever you need access to your database you can import the `prisma` instance into the file where it's needed.

## [Step 5. Update the existing views to load data from the database](https://vercel.com/guides/nextjs-prisma-postgres\#step-5.-update-the-existing-views-to-load-data-from-the-database)

The blog post feed that's implemented in `pages/index.tsx` and the post detail view in `pages/p/[id].tsx` are currently returning hardcoded data. In this step, you'll adjust the implementation to return data from the database using Prisma Client.

Open `pages/index.tsx` and add the following code right below the existing `import` declarations:

pages/index.tsx

```javascript
1import prisma from '../lib/prisma';
```

Import your Prisma Client.

Your `prisma` instance will be your interface to the database when you want to read and write data in it. You can for example create a new `User` record by calling `prisma.user.create()` or retrieve all the `Post` records from the database with `prisma.post.findMany()`. For an overview of the full Prisma Client API, visit the [Prisma docs](https://www.prisma.io/docs/concepts/components/prisma-client/crud).

Now you can replace the hardcoded `feed` object in `getStaticProps` inside `index.tsx` with a proper call to the database:

index.tsx

```javascript
1export const getStaticProps: GetStaticProps = async () => {

2  const feed = await prisma.post.findMany({

3    where: { published: true },

4    include: {

5      author: {

6        select: { name: true },

7      },

8    },

9  });

10  return {

11    props: { feed },

12    revalidate: 10,

13  };

14};
```

Find all published posts in your database.

The two things to note about the Prisma Client query:

- A `where` filter is specified to include only `Post` records where `published` is `true`
- The `name` of the `author` of the `Post` record is queried as well and will be included in the returned objects

Before running the app, head over to `/pages/p/[id].tsx` and adjust the implementation there as well to read the correct `Post` record from the database.

This page uses `getServerSideProps` (SSR) instead of `getStaticProps` (SSG). This is because the data is _dynamic_, it depends on the `id` of the `Post` that's requested in the URL. For example, the view on route `/p/42` displays the `Post` where the `id` is `42`.

Like before, you first need to import Prisma Client on the page:

pages/p/\[id\].tsx

```javascript
1import prisma from '../../lib/prisma';
```

Import your Prisma Client.

Now you can update the implementation of `getServerSideProps` to retrieve the proper post from the database and make it available to your frontend via the component's `props`:

pages/p/\[id\].tsx

```javascript
1export const getServerSideProps: GetServerSideProps = async ({ params }) => {

2  const post = await prisma.post.findUnique({

3    where: {

4      id: String(params?.id),

5    },

6    include: {

7      author: {

8        select: { name: true },

9      },

10    },

11  });

12  return {

13    props: post,

14  };

15};
```

Find a specific post based on the ID.

That's it! If your app is not running any more, you can restart it with the following command:

```bash
1npm run dev
```

Start your application at <http://localhost:3000>.

Otherwise, save the files and open the app at `http://localhost:3000` in your browser. The `Post` record will be displayed as follows:

![Your newly published post.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F11i7qnImXEGxOifqJgTbSJ%2Fc4a13562edb18c54a3c39b28898c8459%2F4.png&w=3840&q=75)

Your newly published post.

You can also click on the post to navigate to its detail view.

## [Step 6. Set up GitHub authentication with NextAuth](https://vercel.com/guides/nextjs-prisma-postgres\#step-6.-set-up-github-authentication-with-nextauth)

In this step, you will add GitHub authentication to the app. Once that functionality is available, you'll add more features to the app, such that authenticated users can create, publish and delete posts via the UI.

As a first step, go ahead and install the NextAuth.js library in your app:

```bash
1npm install next-auth@4 @next-auth/prisma-adapter
```

Install the NextAuth library and the NextAuth Prisma Adapter.

Next, you need to change your database schema to add the missing tables that are [required by NextAuth](https://next-auth.js.org/getting-started/upgrade-v4#postgres).

To change your database schema, you can manually make changes to your Prisma schema and then run the `prisma db push` command again. Open `schema.prisma` and adjust the models in it to look as follows:

```text
1// schema.prisma

2

3model Post {

4  id        String  @id @default(cuid())

5  title     String

6  content   String?

7  published Boolean @default(false)

8  author    User?@relation(fields:[authorId], references:[id])

9  authorId  String?}

10

11model Account {

12  id                 String  @id @default(cuid())

13  userId             String  @map("user_id")

14  type               String

15  provider           String

16  providerAccountId  String  @map("provider_account_id")

17  refresh_token      String?

18  access_token       String?

19  expires_at         Int?

20  token_type         String?

21  scope              String?

22  id_token           String?

23  session_state      String?

24  oauth_token_secret String?

25  oauth_token        String?

26

27  user User @relation(fields:[userId], references:[id], onDelete: Cascade)

28

29  @@unique([provider, providerAccountId])}

30

31model Session {

32  id           String   @id @default(cuid())

33  sessionToken String   @unique@map("session_token")

34  userId       String   @map("user_id")

35  expires      DateTime

36  user         User     @relation(fields:[userId], references:[id], onDelete: Cascade)}

37

38model User {

39  id            String    @id @default(cuid())

40  name          String?

41  email         String?@unique

42  emailVerified DateTime?

43  image         String?

44  posts         Post[]

45  accounts      Account[]

46  sessions      Session[]}

47

48model VerificationToken {

49  id         Int      @id @default(autoincrement())

50  identifier String

51  token      String   @unique

52  expires    DateTime

53

54  @@unique([identifier, token])}

55}
```

Updated Prisma schema.

To learn more about these models, visit the [NextAuth.js docs](https://next-auth.js.org/schemas/models).

Now you can adjust your database schema by creating the actual tables in the database. Run the following command:

```bash
1npx prisma db push
```

Update the tables in your database based on your Prisma schema.

Since you're using GitHub authentication, you also need to create a new [OAuth app on GitHub](https://docs.github.com/en/free-pro-team@latest/developers/apps/building-oauth-apps). First, log into your [GitHub](https://github.com/) account. Then, navigate to [**Settings**](https://github.com/settings/profile), then open to [**Developer Settings**](https://github.com/settings/apps), then switch to [**OAuth Apps**](https://github.com/settings/developers).

![Create a new OAuth application inside GitHub.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F42WGp7BsBEk2we6u3nx9O7%2F1bea8b695cf0e40081b7f2187244791b%2F5.png&w=3840&q=75)

Create a new OAuth application inside GitHub.

Clicking on the **Register a new application** (or **New OAuth App**) button will redirect you to a registration form to fill out some information for your app. The **Authorization callback URL** should be the Next.js `/api/auth` route: `http://localhost:3000/api/auth`.

An important thing to note here is that the **Authorization callback URL** field only supports a single URL, unlike e.g. Auth0, which allows you to add additional callback URLs separated with a comma. This means if you want to deploy your app later with a production URL, you will need to set up a new GitHub OAuth app.

![Ensure your Authorization callback URL is correct.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F1N0WpTZ8HAR9k7qSVpfgfl%2F8854fd577bf09916b88493b8734db245%2F6.png&w=3840&q=75)

Ensure your Authorization callback URL is correct.

Click on the **Register application** button, and then you will be able to find your newly generated **Client ID** and **Client Secret**. Copy and paste this info into the `.env` file in the root directory as the `GITHUB_ID` and `GITHUB_SECRET` env vars. Also set the `NEXTAUTH_URL` to the same value of the **Authorization callback URL** thar you configured on GitHub: `http://localhost:3000/api/auth`

```bash
1# .env

2

3# GitHub OAuth

4GITHUB_ID=6bafeb321963449bdf51

5GITHUB_SECRET=509298c32faa283f28679ad6de6f86b2472e1bff

6NEXTAUTH_URL=http://localhost:3000/api/auth
```

The completed .env file.

You will also need to persist a user's authentication state across the entire application. Make a quick change in your application's root file `_app.tsx` and wrap your current root component with a `SessionProvider` from the `next-auth/react` package. Open the file and replace its current contents with the following code:

\_app.tsx

```jsx
1import { SessionProvider } from 'next-auth/react';

2import { AppProps } from 'next/app';

3

4const App = ({ Component, pageProps }: AppProps) => {

5  return (

6    <SessionProvider session={pageProps.session}>

7      <Component {...pageProps} />

8    </SessionProvider>

9  );

10};

11

12export default App;
```

Wrap your application with the NextAuth SessionProvider.

## [Step 7. Add Log In functionality](https://vercel.com/guides/nextjs-prisma-postgres\#step-7.-add-log-in-functionality)

The login button and some other UI components will be added to the `Header.tsx` file. Open the file and paste the following code into it:

Header.tsx

```jsx
1import React from 'react';

2import Link from 'next/link';

3import { useRouter } from 'next/router';

4import { signOut, useSession } from 'next-auth/react';

5

6const Header: React.FC = () => {

7  const router = useRouter();

8  const isActive: (pathname: string) => boolean = (pathname) =>

9    router.pathname === pathname;

10

11  const { data: session, status } = useSession();

12

13  let left = (

14    <div className="left">

15      <Link href="/">

16        <a className="bold" data-active={isActive('/')}>

17          Feed

18        </a>

19      </Link>

20      <style jsx>{`

21        .bold {

22          font-weight: bold;

23        }

24

25        a {

26          text-decoration: none;

27          color: var(--geist-foreground);

28          display: inline-block;

29        }

30

31        .left a[data-active='true'] {

32          color: gray;

33        }

34

35        a + a {

36          margin-left: 1rem;

37        }

38      `}</style>

39    </div>

40  );

41

42  let right = null;

43

44  if (status === 'loading') {

45    left = (

46      <div className="left">

47        <Link href="/">

48          <a className="bold" data-active={isActive('/')}>

49            Feed

50          </a>

51        </Link>

52        <style jsx>{`

53          .bold {

54            font-weight: bold;

55          }

56

57          a {

58            text-decoration: none;

59            color: var(--geist-foreground);

60            display: inline-block;

61          }

62

63          .left a[data-active='true'] {

64            color: gray;

65          }

66

67          a + a {

68            margin-left: 1rem;

69          }

70        `}</style>

71      </div>

72    );

73    right = (

74      <div className="right">

75        <p>Validating session ...</p>

76        <style jsx>{`

77          .right {

78            margin-left: auto;

79          }

80        `}</style>

81      </div>

82    );

83  }

84

85  if (!session) {

86    right = (

87      <div className="right">

88        <Link href="/api/auth/signin">

89          <a data-active={isActive('/signup')}>Log in</a>

90        </Link>

91        <style jsx>{`

92          a {

93            text-decoration: none;

94            color: var(--geist-foreground);

95            display: inline-block;

96          }

97

98          a + a {

99            margin-left: 1rem;

100          }

101

102          .right {

103            margin-left: auto;

104          }

105

106          .right a {

107            border: 1px solid var(--geist-foreground);

108            padding: 0.5rem 1rem;

109            border-radius: 3px;

110          }

111        `}</style>

112      </div>

113    );

114  }

115

116  if (session) {

117    left = (

118      <div className="left">

119        <Link href="/">

120          <a className="bold" data-active={isActive('/')}>

121            Feed

122          </a>

123        </Link>

124        <Link href="/drafts">

125          <a data-active={isActive('/drafts')}>My drafts</a>

126        </Link>

127        <style jsx>{`

128          .bold {

129            font-weight: bold;

130          }

131

132          a {

133            text-decoration: none;

134            color: var(--geist-foreground);

135            display: inline-block;

136          }

137

138          .left a[data-active='true'] {

139            color: gray;

140          }

141

142          a + a {

143            margin-left: 1rem;

144          }

145        `}</style>

146      </div>

147    );

148    right = (

149      <div className="right">

150        <p>

151          {session.user.name} ({session.user.email})

152        </p>

153        <Link href="/create">

154          <button>

155            <a>New post</a>

156          </button>

157        </Link>

158        <button onClick={() => signOut()}>

159          <a>Log out</a>

160        </button>

161        <style jsx>{`

162          a {

163            text-decoration: none;

164            color: var(--geist-foreground);

165            display: inline-block;

166          }

167

168          p {

169            display: inline-block;

170            font-size: 13px;

171            padding-right: 1rem;

172          }

173

174          a + a {

175            margin-left: 1rem;

176          }

177

178          .right {

179            margin-left: auto;

180          }

181

182          .right a {

183            border: 1px solid var(--geist-foreground);

184            padding: 0.5rem 1rem;

185            border-radius: 3px;

186          }

187

188          button {

189            border: none;

190          }

191        `}</style>

192      </div>

193    );

194  }

195

196  return (

197    <nav>

198      {left}

199      {right}

200      <style jsx>{`

201        nav {

202          display: flex;

203          padding: 2rem;

204          align-items: center;

205        }

206      `}</style>

207    </nav>

208  );

209};

210

211export default Header;
```

Allow the user to log in through the Header.

Here's an overview of how the header is going to render:

- If no user is authenticated, a **Log in** button will be shown.
- If a user is authenticated, **My drafts**, **New Post** and **Log out** buttons will be shown.

You can already run the app to validate that this works by running `npm run dev`, you'll find that the **Log in** button is now shown. However, if you click it, it does navigate you to `http://localhost:3000/api/auth/signin` but Next.js is going to render a 404 page for you.

That's because [NextAuth.js requires you to set up a specific route for authentication](https://next-auth.js.org/configuration/pages). You'll do that next.

Create a new directory and a new file in the `pages/api` directory:

```bash
1mkdir -p pages/api/auth && touch pages/api/auth/[...nextauth].ts
```

Create a new directory and API route.

In this new `pages/api/auth/[...nextauth].ts` file, you now need to add the following boilerplate to configure your NextAuth.js setup with your GitHub OAuth credentials and the [Prisma adapter](https://next-auth.js.org/schemas/adapters#prisma-adapter):

pages/api/auth/\[...nextauth\].ts

```javascript
1import { NextApiHandler } from 'next';

2import NextAuth from 'next-auth';

3import { PrismaAdapter } from '@next-auth/prisma-adapter';

4import GitHubProvider from 'next-auth/providers/github';

5import prisma from '../../../lib/prisma';

6

7const authHandler: NextApiHandler = (req, res) => NextAuth(req, res, options);

8export default authHandler;

9

10const options = {

11  providers: [\
\
12    GitHubProvider({\
\
13      clientId: process.env.GITHUB_ID,\
\
14      clientSecret: process.env.GITHUB_SECRET,\
\
15    }),\
\
16  ],

17  adapter: PrismaAdapter(prisma),

18  secret: process.env.SECRET,

19};
```

Set up NextAuth, including the Prisma Adapter.

Once the code is added, you can navigate to `http://localhost:3000/api/auth/signin` again. This time, the **Sign in with GitHub** button is shown.

![Sign in with GitHub using NextAuth.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F4kQ9bV1IGBC43DwzvuT1p0%2F2725db72dd59860dc3ace3ee35331e43%2F7.png&w=3840&q=75)

Sign in with GitHub using NextAuth.

If you click it, you're forwarded to GitHub, where you can authenticate with your GitHub credentials. Once the authentication is done, you'll be redirected back into the app.

**Note:** If you're seeing an error and could not be authenticated, stop the app and re-run it with `npm run dev`.

The header layout has now changed to display the buttons for authenticated users.

![The Header displaying a log out button.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F42h50fNeDIOpA6YEH5MVUg%2Fe6f7f16ddbe32520e24bb3dcc107f760%2F8.png&w=3840&q=75)

The Header displaying a log out button.

## [Step 8. Add new post functionality](https://vercel.com/guides/nextjs-prisma-postgres\#step-8.-add-new-post-functionality)

In this step, you'll implement a way for a user to create a new post. The user can use this feature by clicking the **New post** button once they're authenticated.

The button already forwards to the `/create` route, however, this currently leads to a 404 because that route is not implemented yet.

To fix that, create a new file in the pages directory that's called `create.tsx`:

```bash
1touch pages/create.tsx
```

Create a new file for creating posts.

Now, add the following code to the newly created file:

pages/create.tsx

```jsx
1import React, { useState } from 'react';

2import Layout from '../components/Layout';

3import Router from 'next/router';

4

5const Draft: React.FC = () => {

6  const [title, setTitle] = useState('');

7  const [content, setContent] = useState('');

8

9  const submitData = async (e: React.SyntheticEvent) => {

10    e.preventDefault();

11    // TODO

12    // You will implement this next ...

13  };

14

15  return (

16    <Layout>

17      <div>

18        <form onSubmit={submitData}>

19          <h1>New Draft</h1>

20          <input

21            autoFocus

22            onChange={(e) => setTitle(e.target.value)}

23            placeholder="Title"

24            type="text"

25            value={title}

26          />

27          <textarea

28            cols={50}

29            onChange={(e) => setContent(e.target.value)}

30            placeholder="Content"

31            rows={8}

32            value={content}

33          />

34          <input disabled={!content || !title} type="submit" value="Create" />

35          <a className="back" href="#" onClick={() => Router.push('/')}>

36            or Cancel

37          </a>

38        </form>

39      </div>

40      <style jsx>{`

41        .page {

42          background: var(--geist-background);

43          padding: 3rem;

44          display: flex;

45          justify-content: center;

46          align-items: center;

47        }

48

49        input[type='text'],

50        textarea {

51          width: 100%;

52          padding: 0.5rem;

53          margin: 0.5rem 0;

54          border-radius: 0.25rem;

55          border: 0.125rem solid rgba(0, 0, 0, 0.2);

56        }

57

58        input[type='submit'] {

59          background: #ececec;

60          border: 0;

61          padding: 1rem 2rem;

62        }

63

64        .back {

65          margin-left: 1rem;

66        }

67      `}</style>

68    </Layout>

69  );

70};

71

72export default Draft;
```

A new component to create posts.

This page is wrapped by the `Layout` component so that it still includes the `Header` and any other generic UI components.

It renders a form with several input fields. When submitted, the (right now empty) `submitData` function is called. In that function, you need to pass the data from the React component to an API route which can then handle the actual storage of the new post data in the database.

Here's how you can implement the function:

pages/create.tsx

```javascript
1const submitData = async (e: React.SyntheticEvent) => {

2  e.preventDefault();

3  try {

4    const body = { title, content };

5    await fetch('/api/post', {

6      method: 'POST',

7      headers: { 'Content-Type': 'application/json' },

8      body: JSON.stringify(body),

9    });

10    await Router.push('/drafts');

11  } catch (error) {

12    console.error(error);

13  }

14};
```

Call your API route to create a post.

In this code, you're using the `title` and `content` properties that are extracted from the component state using `useState` and submit them via an HTTP POST request to the `api/post` API route.

Afterwards, you're redirecting the user to the `/drafts` page so that they can immediately see their newly created draft. If you run the app, the `/create` route renders the following UI:

![Create a new draft.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F282p7LTOlQRXTV4CJzzfxa%2F15b5b92f4ebfb31d791ea5f651503dc0%2F9.png&w=3840&q=75)

Create a new draft.

Note however that the implementation doesn't quite work yet because neither `api/post` nor the `/drafts` route exist so far. You'll implement these next.

First, let's make sure your backend can handle the POST request that's submitted by the user. Thanks to the [Next.js API routes](https://nextjs.org/docs/api-routes/introduction) feature, you don't have to "leave your Next.js app" to implement such functionality but instead you can add it to your `pages/api` directory.

Create a new directory called `post` with a new file called `index.ts`:

```bash
1mkdir -p pages/api/post && touch pages/api/post/index.ts
```

Create a new API route to create a post.

**Note:** At this point, you could also have created a file called `pages/api/post.ts`\` instead of taking the detour with an extra directory and an `index.ts` file. The reason why you're not doing it that way is because you'll need to add a dynamic route for HTTP `DELETE` requests at the `api/post` route later as well. In order to save some refactoring later, you're already structuring the files in the required way.

Now, add the following code to `pages/api/post/index.ts`:

pages/api/post/index.ts

```javascript
1import { getSession } from 'next-auth/react';

2import prisma from '../../../lib/prisma';

3

4// POST /api/post

5// Required fields in body: title

6// Optional fields in body: content

7export default async function handle(req, res) {

8  const { title, content } = req.body;

9

10  const session = await getSession({ req });

11  const result = await prisma.post.create({

12    data: {

13      title: title,

14      content: content,

15      author: { connect: { email: session?.user?.email } },

16    },

17  });

18  res.json(result);

19}
```

Update the API route to modify the database using the Prisma Client.

This code implements the _handler_ function for any requests coming in at the `/api/post/` route. The implementation does the following: First it extracts the `title` and `cotent` from the body of the incoming HTTP POST request. After that, it checks whether the request is coming from an authenticated user with the `getSession` helper function from NextAuth.js. And finally, it uses Prisma Client to create a new `Post` record in the database.

You can now test this functionality by opening the app, making sure you're authenticated and create a new post with title and content:

![Testing creating a new post via the API Route.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2Z41gYOddxIlo6KwqswDPd%2F99eca6c7deaf23d437c71c8646b7444a%2F10.png&w=3840&q=75)

Testing creating a new post via the API Route.

Once you click **Create**, the `Post` record will be added to the database. Note that the `/drafts` route that you're being redirected to right after the creation still renders a 404, that will be fixed soon. However, if you run Prisma Studio again with `npx prisma studio`, you'll see that the new `Post` record has been added to the database.

## [Step 9. Add drafts functionality](https://vercel.com/guides/nextjs-prisma-postgres\#step-9.-add-drafts-functionality)

In this step, you'll add a new page to the app that allows an authenticated user to view their current _drafts_.

This page can't be statically rendered because it depends on a user who is authenticated. Pages like this that get their data _dynamically_ based on an authenticated users are a great use case for server-side rendering (SSR) via `getServerSideProps`.

First, create a new file in the `pages` directory and call it `drafts.tsx`:

```bash
1touch pages/drafts.tsx
```

Create a new page for your drafts.

Next, add the following code to that file:

pages/drafts.tsx

```jsx
1import React from 'react';

2import { GetServerSideProps } from 'next';

3import { useSession, getSession } from 'next-auth/react';

4import Layout from '../components/Layout';

5import Post, { PostProps } from '../components/Post';

6import prisma from '../lib/prisma';

7

8export const getServerSideProps: GetServerSideProps = async ({ req, res }) => {

9  const session = await getSession({ req });

10  if (!session) {

11    res.statusCode = 403;

12    return { props: { drafts: [] } };

13  }

14

15  const drafts = await prisma.post.findMany({

16    where: {

17      author: { email: session.user.email },

18      published: false,

19    },

20    include: {

21      author: {

22        select: { name: true },

23      },

24    },

25  });

26  return {

27    props: { drafts },

28  };

29};

30

31type Props = {

32  drafts: PostProps[];

33};

34

35const Drafts: React.FC<Props> = (props) => {

36  const { data: session } = useSession();

37

38  if (!session) {

39    return (

40      <Layout>

41        <h1>My Drafts</h1>

42        <div>You need to be authenticated to view this page.</div>

43      </Layout>

44    );

45  }

46

47  return (

48    <Layout>

49      <div className="page">

50        <h1>My Drafts</h1>

51        <main>

52          {props.drafts.map((post) => (

53            <div key={post.id} className="post">

54              <Post post={post} />

55            </div>

56          ))}

57        </main>

58      </div>

59      <style jsx>{`

60        .post {

61          background: var(--geist-background);

62          transition: box-shadow 0.1s ease-in;

63        }

64

65        .post:hover {

66          box-shadow: 1px 1px 3px #aaa;

67        }

68

69        .post + .post {

70          margin-top: 2rem;

71        }

72      `}</style>

73    </Layout>

74  );

75};

76

77export default Drafts;
```

Update the Draft page to show a list of drafts.

In this React component, you're rendering a list of "drafts" of the authenticated user. The drafts are retrieved from the database during server-side rendering, because the database query with Prisma Client is executed in `getServerSideProps`. The data is then made available to the React component via its `props`.

If you now navigate to the **My drafts** section of the app, you'll see the unpublished post that you created before:

![Completed drafts page.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F221Ve9cFpuAu9zBKZVjaWJ%2Fcd6fe2068b187c30220a8f868b767c35%2F11.png&w=3840&q=75)

Completed drafts page.

## [Step 10. Add Publish functionality](https://vercel.com/guides/nextjs-prisma-postgres\#step-10.-add-publish-functionality)

To "move" the draft to the public feed view, you need to be able to "publish" it – that is, setting the `published` field of a `Post` record to `true`. This functionality will be implemented in the post detail view that currently lives in `pages/p/[id].tsx`.

The functionality will be implemented via an HTTP PUT request that'll be sent to a `api/publish` route in your "Next.js backend". Go ahead and implement that route first.

Create a new directory inside the `pages/api` directory called `publish`. Then create a new file called `[id].ts` in the new directory:

```bash
1mkdir -p pages/api/publish && touch pages/api/publish/[id].ts
```

Create a new API route to publish a post.

Now, add the following code to the newly created file:

pages/api/publish/\[id\].ts

```javascript
1import prisma from '../../../lib/prisma';

2

3// PUT /api/publish/:id

4export default async function handle(req, res) {

5  const postId = req.query.id;

6  const post = await prisma.post.update({

7    where: { id: postId },

8    data: { published: true },

9  });

10  res.json(post);

11}
```

Update the API route to modify the database using the Prisma Client.

This is the implementation of an API route handler which retrieves the ID of a `Post` from the URL and then uses Prisma Client's `update` method to set the `published` field of the `Post` record to `true`.

Next, you'll implement the functionality on the frontend in the `pages/p/[id].tsx` file. Open up the file and replace its contents with the following:

pages/p/\[id\].tsx

```jsx
1import React from 'react';

2import { GetServerSideProps } from 'next';

3import ReactMarkdown from 'react-markdown';

4import Router from 'next/router';

5import Layout from '../../components/Layout';

6import { PostProps } from '../../components/Post';

7import { useSession } from 'next-auth/react';

8import prisma from '../../lib/prisma';

9

10export const getServerSideProps: GetServerSideProps = async ({ params }) => {

11  const post = await prisma.post.findUnique({

12    where: {

13      id: String(params?.id),

14    },

15    include: {

16      author: {

17        select: { name: true, email: true },

18      },

19    },

20  });

21  return {

22    props: post,

23  };

24};

25

26async function publishPost(id: string): Promise<void> {

27  await fetch(`/api/publish/${id}`, {

28    method: 'PUT',

29  });

30  await Router.push('/');

31}

32

33const Post: React.FC<PostProps> = (props) => {

34  const { data: session, status } = useSession();

35  if (status === 'loading') {

36    return <div>Authenticating ...</div>;

37  }

38  const userHasValidSession = Boolean(session);

39  const postBelongsToUser = session?.user?.email === props.author?.email;

40  let title = props.title;

41  if (!props.published) {

42    title = `${title} (Draft)`;

43  }

44

45  return (

46    <Layout>

47      <div>

48        <h2>{title}</h2>

49        <p>By {props?.author?.name || 'Unknown author'}</p>

50        <ReactMarkdown children={props.content} />

51        {!props.published && userHasValidSession && postBelongsToUser && (

52          <button onClick={() => publishPost(props.id)}>Publish</button>

53        )}

54      </div>

55      <style jsx>{`

56        .page {

57          background: var(--geist-background);

58          padding: 2rem;

59        }

60

61        .actions {

62          margin-top: 2rem;

63        }

64

65        button {

66          background: #ececec;

67          border: 0;

68          border-radius: 0.125rem;

69          padding: 1rem 2rem;

70        }

71

72        button + button {

73          margin-left: 1rem;

74        }

75      `}</style>

76    </Layout>

77  );

78};

79

80export default Post;
```

Update the Post component to handle publishing via the API Route.

This code adds the `publishPost` function to the React component which is responsible for sending the HTTP PUT request to the API route you just implemented. The `render` function of the component is also adjusted to check whether the user is authenticated, and if that's the case, it'll display the **Publish** button in the post detail view as well:

![The publish button shown for a post.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F1Ohdg5zNejFfXxwWAe6hpR%2F1d7a7059cb51bf3d6f29a66caafd884f%2F12.png&w=3840&q=75)

The publish button shown for a post.

If you click the button, you will be redirected to the public feed and the post will be displayed there!

**Note:** Once the app is deployed to production, the feed will be updated at most every 10 seconds when it receives a request. That's because you're using static site generation (SSG) via `getStaticProps` to retrieve the data for this view with [Incremental Static Regeneration](https://vercel.com/docs/basic-features/data-fetching/incremental-static-regeneration). If you want data to be updated "immediately", consider using [On-Demand Incremental Static Regeneration](https://vercel.com/docs/concepts/incremental-static-regeneration/quickstart).

## [Step 11. Add Delete functionality](https://vercel.com/guides/nextjs-prisma-postgres\#step-11.-add-delete-functionality)

The last piece of functionality you'll implement in this guide is to enable users to delete existing `Post` records. You'll follow a similar approach as for the "publish" functionality by first implementing the API route handler on the backend, and then adjust your frontend to make use of the new route!

Create a new file in the `pages/api/post` directory and call it `[id].ts`:

```bash
1touch pages/api/post/[id].ts
```

Create a new API route to delete a post.

Now, add the following code to it:

pages/api/post/\[id\].ts

```javascript
1import prisma from '../../../lib/prisma';

2

3// DELETE /api/post/:id

4export default async function handle(req, res) {

5  const postId = req.query.id;

6  if (req.method === 'DELETE') {

7    const post = await prisma.post.delete({

8      where: { id: postId },

9    });

10    res.json(post);

11  } else {

12    throw new Error(

13      `The HTTP ${req.method} method is not supported at this route.`,

14    );

15  }

16}
```

Update the API route to modify the database using the Prisma Client.

This code handles HTTP `DELETE` requests that are coming in via the `/api/post/:id` URL. The route handler then retrieves the `id` of the `Post` record from the URL and uses Prisma Client to delete this record in the database.

To make use of this feature on the frontend, you again need to adjust the post detail view. Open `pages/p/[id].tsx` and insert the following function right below the `publishPost` function:

pages/p/\[id\].tsx

```javascript
1async function deletePost(id: string): Promise<void> {

2  await fetch(`/api/post/${id}`, {

3    method: 'DELETE',

4  });

5  Router.push('/');

6}
```

Update the Post component to handle deleting via the API Route.

Now, you can follow a similar approach with the **Delete** button as you did with the **Publish** button and render it only if the user is authenticated. To achieve this, you can add this code directly in the `return` part of the `Post` component right below where the **Publish** button is rendered:

```jsx
1// pages/p/[id].tsx

2{

3  !props.published && userHasValidSession && postBelongsToUser && (

4    <button onClick={() => publishPost(props.id)}>Publish</button>

5  );

6}

7{

8  userHasValidSession && postBelongsToUser && (

9    <button onClick={() => deletePost(props.id)}>Delete</button>

10  );

11}
```

Logic to determine whether to show the publish and delete buttons.

You can now try out the new functionality by creating a new draft, navigating to its detail view and then clicking the newly appearing **Delete** button:

![The Delete button showing on the post page.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5yf3vrKOb7i56gMZY7zJQA%2F94975799afd8fa6cbe460e9301bc389d%2F13.png&w=3840&q=75)

The Delete button showing on the post page.

## [Step 12. Deploy to Vercel](https://vercel.com/guides/nextjs-prisma-postgres\#step-12.-deploy-to%C2%A0vercel)

In this final step, you're going to deploy the app to Vercel from a GitHub repo.

Before you can deploy, you need to:

- Create another OAuth app on GitHub
- Create a new GitHub repo and push your project to it

To start with the OAuth app, go back to step "Step 5. Set up GitHub authentication with NextAuth" and follow the steps to create another OAuth app via the GitHub UI.

This time, the **Authorization Callback URL** needs to match the domain of your future Vercel deployment which will be based on the Vercel project name. As a Vercel project name, you will choose `blogr-nextjs-prisma` prepended with your first and lastname: `FIRSTNAME-LASTNAME-blogr-nextjs-prisma`. For example, if you're called "Jane Doe", your project name should be `jane-doe-blogr-nextjs-prisma`.

**Note:** Prepending your first and last name is required to ensure the uniqueness of your deployment URL.

The **Authorization Callback URL** must therefore be set to `https://FIRSTNAME-LASTNAME-blogr-nextjs-prisma.vercel.app/api/auth`. Once you created the application, adjust your `.env` file and set the **Client ID** as the `GITHUB_ID` env var and a **Client secret** as the `GITHUB_SECRET` env var. The `NEXTAUTH_URL` env var needs to be set to the same value as the **Authorization Callback URL** on GitHub: `https://FIRSTNAME-LASTNAME-blogr-nextjs-prisma.vercel.app/api/auth`.

![Update the Authorization callback URL.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F4eKx9gXLs1BDg0UpX6pfsz%2Fd3fe7b9905a49f3913b8528449f161d3%2F14.png&w=3840&q=75)

Update the Authorization callback URL.

Next, create a new GitHub repository with the same name, e.g. `jane-doe-blogr-nextjs-prisma`. Now, copy the three terminal commands from the bottom section that says **...or push an existing repository from the command line**, it should look similar to this:

```bash
1git remote add origin git@github.com:janedoe/jane-doe-blogr-nextjs-prisma.git

2git branch -M main

3git push -u origin main
```

Push to an existing repository.

You now should have your new repository ready at `https://github.com/GITHUB_USERNAME/FIRSTNAME-LASTNAME-blogr-nextjs-prisma`, e.g. `https://github.com/janedoe/jane-doe-blogr-nextjs-prisma`.

With the GitHub repo in place, you can now import it to Vercel in order to deploy the app:

[![Deploy](https://images.ctfassets.net/e5382hct74si/1MBW5fsAqJiqhbfdOPKzzm/96dc8bdc471276d0a086fee9c475890b/button.svg)\\
\\
Deploy](https://vercel.com/import/git?env=DATABASE_URL,GITHUB_ID,GITHUB_SECRET,NEXTAUTH_URL)

Now, provide the URL of your GitHub repo in the text field:

![Import a git repository to Vercel.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F3B7J88ffcf3qs9Bha2dXzM%2F0cb1d6a68e7aeacb2d4e0b4cad8abe8d%2F15.png&w=3840&q=75)

Import a git repository to Vercel.

Click **Continue**. The next screen requires you to set the environment variables for your production deployment:

![Add environment variables to Vercel.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5sGJJuC4IwP36gk1bKUpqP%2Fa6ca4c68a304336a11a3961918f31639%2F16.png&w=3840&q=75)

Add environment variables to Vercel.

Here's what you need to provide:

- `GITHUB_ID`: Set this to the **Client ID** of the GitHub OAuth app you just created
- `GITHUB_SECRET`: Set this to the **Client Secret** of the GitHub OAuth app you just created
- `NEXTAUTH_URL`: Set this to the **Authorization Callback URL** of the GitHub OAuth app you just created
- `SECRET`: Set this to your own strong secret. This was not needed in development as NextAuth.js will generate one if not provided. However, you will need to provide your own value for production otherwise you will receive an error.

You'll also need to link your Vercel postgres database to this Vercel project so that all your database environment variables are automatically added. Once all environment variables are set, hit **Deploy**. Your app is now being deployed to Vercel. Once it's ready, Vercel will show you the following success screen:

![Your application deployed to Vercel.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2Fyrw2Jce5AvD3uaa1zZWUl%2Fb28ccffc1601fd441cee1f21a504fc1c%2F17.png&w=3840&q=75)

Your application deployed to Vercel.

You can click the **Visit** button to view the deployed version of your fullstack app 🎉

## [Conclusion](https://vercel.com/guides/nextjs-prisma-postgres\#conclusion)

In this guide, you learned how to build and deploy a fullstack application using Next.js, Prisma, and Vercel Postgres. If you ran into issue or have any questions about this guide, feel free to raise them on [GitHub](https://github.com/prisma/prisma/discussions).

Was this helpful?

supported.

Send
