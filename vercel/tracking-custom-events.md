# Tracking custom events

Custom Events are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Vercel Web Analytics allows you to track custom events in your application using the `track()` function. This is useful for tracking user interactions, such as button clicks, form submissions, or purchases.

Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).

## [Tracking a client-side event](#tracking-a-client-side-event)

To track an event:

1. Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).

2. Import `{ track }` from `@vercel/analytics`.

3. In most cases you will want to track an event when a user performs an action, such as clicking a button or submitting a form, so you should use this on the button handler.

4. Call `track` and pass in a string representing the event name as the first argument. You can also pass [custom data](#tracking-an-event-with-custom-data) as the second argument:

    component.ts

    ```
    import { track } from '@vercel/analytics';
     
    // Call this function when a user clicks a button or performs an action you want to track
    track('Signup');
    ```

This will track an event named **Signup**.

For example, if you have a button that says Sign Up, you can track an event when the user clicks the button:

components/button.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { track } from '@vercel/analytics';
 
function SignupButton() {
  return (
    <button
      onClick={() => {
        track('Signup');
        // ... other logic
      }}
    >
      Sign Up
    </button>
  );
}
```

## [Tracking an event with custom data](#tracking-an-event-with-custom-data)

You can also pass custom data along with an event. To do so, pass an object with key-value pairs as the second argument to `track()`:

component.ts

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
track('Signup', { location: 'footer' });
track('Purchase', { productName: 'Shoes', price: 49.99 });
```

This tracks a "Signup" event that occurred in the "footer" location. The second event tracks a "Purchase" event with product name and a price.

## [Tracking a server-side event](#tracking-a-server-side-event)

In scenarios such as when a user signs up or makes a purchase, it's more useful to track an event on the server-side. For this, you can use the `track` function on API routes or server actions.

To set up server-side events:

1. Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).
2. Import `{ track }` from `@vercel/analytics/server`.
3. Use the `track` function in your API routes or server actions.
4. Pass in a string representing the event name as the first argument to the `track` function. You can also pass [custom data](#tracking-an-event-with-custom-data) as the second argument.

For example, if you want to track a purchase event:

app/actions.ts

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
'use server';
import { track } from '@vercel/analytics/server';
 
export async function purchase() {
  await track('Item purchased', {
    quantity: 1,
  });
}
```

## [Limitations](#limitations)

The following limitations apply to custom data:

* The number of custom data properties you can pass is limited based on your [plan](/docs/analytics/limits-and-pricing).
* Nested objects are not supported.
* Allowed values are `strings`, `numbers`, `booleans`, and `null`.
* You cannot set event name, key, or values to longer than 255 characters each.

## [Tracking custom events in the dashboard](#tracking-custom-events-in-the-dashboard)

Once you have tracked an event, you can view and filter for it in the dashboard. To view your events:

1. Go to your [dashboard](/dashboard), select your project, and click the Analytics tab.
2. From the Web Analytics page, scroll to the Events panel.
3. The events panel displays a list of all the event names that you have created in your project. Select the event name to drill down into the event data.
4. The event details page displays a list, organized by custom data properties, of all the events that have been tracked.
