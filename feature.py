import platform
import psutil
import time
import os


def get_system_info():
    """Get comprehensive system information"""
    try:
        os_name = platform.system()
        os_version = platform.version()
        cpu_count = os.cpu_count()
        memory = psutil.virtual_memory()
        uptime = time.time() - psutil.boot_time()
        uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime))

        return {
            "OS": f"{os_name} {os_version}",
            "CPU Cores": cpu_count,
            "Memory": f"{round(memory.total / (1024 ** 3), 2)} GB",
            "Uptime": uptime_str
        }
    except Exception as e:
        return {"Error": str(e)}


def generate_system_info_html(hostname, ip_address, time_now):
    """Generate HTML with system information"""
    try:
        sys_info = get_system_info()

        sys_info_html = "".join(
            f"<p><strong>{key}:</strong> {value}</p>" for key, value in sys_info.items()
        )

        return f"""
            <h1>Hello from DevOps!</h1>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>IP Address:</strong> {ip_address}</p>
            <p><strong>Timestamp:</strong> {time_now}</p>
            <h2>System Info</h2>
            {sys_info_html}
        """
    except Exception as e:
        return f"""
            <h1>Hello from DevOps!</h1>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>IP Address:</strong> {ip_address}</p>
            <p><strong>Timestamp:</strong> {time_now}</p>
            <h2>System Info</h2>
            <p><strong>Error:</strong> {str(e)}</p>
        """
