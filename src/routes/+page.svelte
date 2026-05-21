<script>
    // TS is not ai trust
    import Header from "$lib/components/header.svelte"
    import Info from "$lib/components/info.svelte"
    import Preview from "$lib/components/preview.svelte"
    import Record from "$lib/components/record.svelte"
    import Controls from "$lib/components/controls.svelte";
</script>
<nav>
    <Header />
</nav>
<main class="m-4">
    <div class="grid gap-4 grid-cols-1 md:grid-cols-2">
        <Info />
        <Preview />
        <Record />
        <Controls />
    </div>
</main>