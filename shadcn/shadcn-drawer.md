# Shadcn Drawer

URL: /ui/drawer
React drawer component for mobile slide-out panels and navigation menus. Built with TypeScript and Tailwind CSS for Next.js applications using Vaul library.

Ever tried to fit a mobile navigation menu into a tiny hamburger dropdown? Or watched users struggle to complete forms on small screens because your modal covers everything? Yeah, cramming desktop UI patterns into mobile doesn't work. This shadcn/ui drawer brings native app-style slide-out panels to your React applications.

### Drawer showcase

Panels that slide naturally like native mobile apps:

<Preview path="ui/drawer-demo" />

Built on Vaul by Emil Kowalski—the same gesture-driven approach used in Linear, Vercel, and other mobile-first applications. Styled with Tailwind CSS so it matches your design system instead of looking like a generic slide menu.

```bash
npx shadcn@latest add drawer
```

## Why drawers actually solve mobile UI problems

Here's the thing—mobile users expect different interactions than desktop users. They swipe, pinch, and drag. They use their thumbs, not precise mouse cursors. A modal that works perfectly on desktop feels alien on mobile. Drawers match how people actually use their phones.

Think about how you use your phone's control center or notification panel. You swipe up from bottom, see your content, swipe again to dismiss. That's muscle memory. This free shadcn drawer brings that familiar interaction pattern to your web apps.

Drawers also solve the space problem. Instead of shrinking your content to fit a modal, drawers slide over it. Users can see what's underneath, dismiss with a gesture, and never lose context. Whether you're building mobile-first interfaces, progressive web apps, or responsive designs in your Next.js applications, drawers that feel native keep users engaged in your JavaScript projects.

## Common drawer patterns you'll actually use

### Simple confirmation

Quick actions and confirmations:

<Preview path="ui/drawer-simple" />

### Responsive dialog-drawer

Smart component that adapts to screen size:

<Preview path="ui/drawer-responsive" />

### Controlled state

Programmatic drawer visibility control:

<Preview path="ui/drawer-controlled" />

### Multiple directions

Slide from any edge of the screen:

<Preview path="ui/drawer-directions" />

### Nested drawers

Layer drawers for complex workflows:

<Preview path="ui/drawer-nested" />

## Features

This free open source drawer component includes everything you need:

- **TypeScript-first** - Full type safety with gesture events and state management
- **Vaul powered** - Physics-based animations and native-feeling interactions
- **Gesture responsive** - Swipe to open, drag to resize, tap to dismiss
- **Tailwind CSS styled** - Customize with utilities, not fighting component CSS
- **Keyboard accessible** - Tab navigation, Escape to close, focus management
- **Multi-directional** - Slide from bottom, top, left, or right edges
- **Snap points** - Multiple height positions for flexible content display
- **Mobile optimized** - Touch targets and gestures designed for thumbs

## API Reference

### Core Components

| Component | Purpose | Key Props |
| --- | --- | --- |
| `Drawer` | Root container | `open`, `onOpenChange`, `direction`, `modal` |
| `DrawerTrigger` | Button that opens | `asChild` for custom triggers |
| `DrawerContent` | Sliding panel | Main content area |
| `DrawerHeader` | Title section | Groups title and description |
| `DrawerFooter` | Action buttons | Typically Submit/Cancel |
| `DrawerClose` | Close button | `asChild` for custom styling |

### Direction Options

| Direction | Use Case | Behavior |
| --- | --- | --- |
| `bottom` | Mobile forms, actions | Slides up from bottom |
| `top` | Notifications, alerts | Slides down from top |
| `left` | Navigation menus | Slides in from left |
| `right` | Shopping carts, settings | Slides in from right |

### Gesture Controls

| Gesture | Action |
| --- | --- |
| **Tap trigger** | Open drawer |
| **Drag handle** | Resize drawer |
| **Swipe opposite** | Close drawer |
| **Tap backdrop** | Close drawer |
| **Escape key** | Close drawer |

## Production tips

**Choose the right direction.** This free shadcn/ui drawer works from any edge, but users have expectations. Bottom drawers feel natural for mobile actions like sharing or forms. Left/right drawers work for navigation. Your React component supports all directions—pick based on user mental models, not visual preference.

**Make gestures discoverable.** Users expect to drag the handle, but they need to see it first. Include a visual drag indicator or subtle animation hint. This TypeScript component provides the gestures—you provide the visual cues that teach users the interaction patterns.

**Handle keyboard users.** Touch gestures are great, but keyboard users need alternatives. Include visible close buttons, proper focus management, and Tab navigation. This open source shadcn component manages focus—you ensure all functionality is accessible in your Next.js applications.

**Test on real devices.** Drawer interactions feel different on actual phones versus browser dev tools. Thumb reach, screen size, and gesture sensitivity matter. The Tailwind CSS component is responsive, but test with real fingers on real screens.

**Consider desktop alternatives.** Drawers shine on mobile but can feel awkward on desktop. Maybe use [Dialog](/ui/dialog) components above certain breakpoints. Your JavaScript application should adapt to the device, not force mobile patterns everywhere.

## Integration with other components

Drawers naturally work with [Button](/ui/button) components for triggers and actions in your React applications. Use [Form](/ui/form) components inside drawer content for data collection with proper validation.

For navigation patterns, combine drawers with [NavigationMenu](/ui/navigation-menu) components to create mobile-first sidebar experiences. [Separator](/ui/separator) components help organize drawer content into logical sections. This open source pattern keeps your mobile interfaces clean and navigable.

When building responsive layouts, pair drawers with [Dialog](/ui/dialog) components—drawer on mobile, dialog on desktop. [Sheet](/ui/sheet) components offer similar slide-out functionality with different styling. Your JavaScript application can choose the right pattern for each screen size.

For content organization, use drawers with [Tabs](/ui/tabs) components for multi-section forms or [Accordion](/ui/accordion) components for collapsible content. The drawer provides the container—other shadcn components handle the internal structure.

## Questions you might have

<Accordions type="single">
  <Accordion id="drawer-vs-dialog" title="When should I use Drawer vs Dialog?">
    Use drawers for mobile-first experiences where gestures matter. Use dialogs for desktop-focused modal interactions. The shadcn drawer feels native on touch devices—dialogs work better with mouse and keyboard interactions.
  </Accordion>

  <Accordion id="drawer-vs-sheet" title="What's the difference between Drawer and Sheet?">
    Both create slide-out panels, but drawer focuses on mobile gestures and snap points. Sheet is more traditional modal overlay. Use drawer when you want native app-like interactions, sheet for simpler slide-in content panels.
  </Accordion>

  <Accordion id="drawer-snap-points" title="How do snap points work?">
    Snap points let drawers stop at specific heights like 50% or 80% of screen. Users can drag to resize, and the drawer snaps to your defined positions. This free shadcn component handles the physics—you define the stopping points that make sense for your content.
  </Accordion>

  <Accordion id="drawer-accessibility" title="Are drawers accessible to screen readers?">
    Yes, the component uses proper ARIA roles and manages focus correctly. Screen readers announce when drawers open/close and can navigate content normally. But accessibility depends on your content—use clear headings and logical tab order in your Next.js application.
  </Accordion>

  <Accordion id="drawer-nested" title="Can I nest multiple drawers?">
    The component supports nesting, but use it carefully. Users can lose context with too many layers. Consider single drawer with internal navigation instead. If you do nest, ensure clear visual hierarchy and easy escape routes back to parent levels.
  </Accordion>

  <Accordion id="drawer-performance" title="Do drawers impact performance?">
    Drawers are lightweight and use efficient animations. For content-heavy drawers, consider lazy loading. The TypeScript component itself is optimized—performance issues usually come from heavy content or too many simultaneous animations.
  </Accordion>

  <Accordion id="drawer-responsive" title="How do I make drawers responsive?">
    Use the responsive pattern example or conditionally render drawer vs dialog based on screen size. The open source component works on all devices, but you might want different patterns for different screen sizes in your React application.
  </Accordion>

  <Accordion id="drawer-custom-animations" title="Can I customize drawer animations?">
    The component uses physics-based animations from Vaul. You can adjust timing and easing through Tailwind CSS classes or custom CSS. The default animations feel natural, but you can match your brand's motion design while keeping the gesture responsiveness.
  </Accordion>
</Accordions>
