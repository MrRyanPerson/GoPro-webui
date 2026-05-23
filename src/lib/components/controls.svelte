<script>
    async function clearGopros() {
        try {
            if (confirm("Would you like to clear all saved media on all GoPros?")) {
                await fetch('http://localhost:8000/controls/clear_gopros');
            }
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
    async function setKeepAlive() {
        try {
            await fetch('http://localhost:8000/controls/set_keep_alive');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }

</script>

<div class="p-4 rounded-box shadow-sm bg-base-200">
    <h1 class="text-2xl m-2 font-bold text-content">Extra Controls</h1>
    <div class="grid gap-2 grid-cols-2 sm:grid-cols-3">
        <button class="btn btn-block" onclick={clearGopros}>
            Clear GoPro
        </button>
        <button class="btn btn-block" onclick={setKeepAlive}>
            Keep Alive
        </button>
    </div>
</div>