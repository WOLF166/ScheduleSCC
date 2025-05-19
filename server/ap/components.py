import asyncio
from asgiref.sync import sync_to_async
from reactpy import component, html, use_state, use_effect
import logging
import requests
from datetime import date


# Асинхронные функции для получения данных
@sync_to_async
def fetch_schedule_data(group):
    try:
        response = requests.get(f'http://176.108.253.4:8000/getScheduleGroup?group={group}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Schedule request failed: {e}")
        return []


@sync_to_async
def fetch_groups():
    try:
        response = requests.get(f'http://176.108.253.4:8000/getAllGroup')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Groups request failed: {e}")
        return []


# Стили (подобраны под цвета герба колледжа)
main_style = {
    "fontFamily": "Segoe UI, Arial, sans-serif",
    "background": "#f8f9fa",
    "minHeight": "100vh",
    "padding": "0",
    "margin": "0",
    "display": "flex",
    "flexDirection": "column",
}

header_style = {
    "background": "#0055A5",
    "color": "#fff",
    "padding": "2rem 0 1rem 0",
    "textAlign": "center",
    "boxShadow": "0 4px 12px rgba(0,0,0,0.07)",
}

footer_style = {
    "background": "#0055A5",
    "color": "white",
    "padding": "1rem",
    "textAlign": "center",
    "marginTop": "auto",
}

filter_container = {
    "display": "flex",
    "gap": "1rem",
    "justifyContent": "center",
    "margin": "1.5rem 0",
    "flexWrap": "wrap",
}

select_style = {
    "padding": "0.5rem 1rem",
    "borderRadius": "7px",
    "border": "1px solid #ced4da",
    "backgroundColor": "#fff",
    "color": "#212529",
    "fontSize": "1rem",
    "minWidth": "200px",
    "boxShadow": "0 2px 4px rgba(0,0,0,0.05)",
}

# Общие стили для ячеек таблицы (td)
td_base_style = {
    "padding": "1rem",
    "borderBottom": "1px solid #dee2e6",
    "textAlign": "center",
}

# Общие стили для заголовков таблицы (th)
th_base_style = {
    "padding": "1rem",
    "background": "#0055A5",
    "color": "white",
    "textAlign": "center",
}

# Стили таблицы
table_style = {
    "width": "90%",
    "margin": "0 auto",
    "borderCollapse": "collapse",
    "backgroundColor": "#fff",
    "boxShadow": "0 1px 3px rgba(0,0,0,0.1)"
}


# Компонент расписания
@component
def ScheduleComponent():
    schedules, set_schedules = use_state([])
    groups, set_groups = use_state([])
    selected_date, set_selected_date = use_state(date.today().isoformat())
    selected_group, set_selected_group = use_state("")

    async def load_data():
        # Загрузка групп при монтировании
        groups_data = await fetch_groups()
        set_groups(groups_data)

        if groups_data:
            # Установка первой группы по умолчанию
            first_group_name = groups_data[0]['name']
            set_selected_group(first_group_name)

            # ID для запроса расписания
            first_group_id = groups_data[0]['id']
            schedule_data = await fetch_schedule_data(first_group_id)
            set_schedules(schedule_data)

    def start_load_data():
        asyncio.create_task(load_data())

    use_effect(start_load_data, [])

    # Обработчик изменения группы
    async def handle_group_change(e):
        group_name = e['target']['value']
        set_selected_group(group_name)

        group_id = None
        for g in groups:
            if g['name'] == group_name:
                group_id = g['id']
                break

        if group_id is not None:
            data = await fetch_schedule_data(group_id)
            set_schedules(data)

    # Фильтрация расписания
    filtered = [
        item for item in schedules
        if item.get("day") == selected_date and item.get("group") == selected_group
    ]

    return html.div(
        {"style": main_style},
        html.header(
            {"style": header_style},
            html.h1("Расписание занятий"),
            html.p("Выберите группу и дату")
        ),
        html.div(
            {"style": filter_container},
            html.select({
                "value": selected_group,
                "onChange": handle_group_change,
                "style": select_style
            },
                [html.option({"value": group['name']}, group['name']) for group in groups]
            ),
            html.input({
                "type": "date",
                "value": selected_date,
                "onChange": lambda e: set_selected_date(e["target"]["value"]),
                "style": select_style
            })
        ),
        html.div(
            html.table(
                {"style": table_style},
                html.thead(
                    html.tr(
                        html.th({"style": th_base_style}, "Кабинет"),
                        html.th({"style": th_base_style}, "Предмет"),
                        html.th({"style": th_base_style}, "Преподаватель"),
                        html.th({"style": th_base_style}, "Время"),
                    )
                ),
                html.tbody(
                    [html.tr(
                        html.td({"style": td_base_style}, item["room"]),
                        html.td({"style": td_base_style}, item["subject"]),
                        html.td({"style": td_base_style}, item["teacher"]),
                        html.td({"style": td_base_style}, item["startTime"]),
                    ) for item in filtered] if filtered else [
                        html.tr(
                            html.td(
                                {"colSpan": 4, "style": {"textAlign": "center", "padding": "2rem", "color": "#6c757d"}},
                                "Нет занятий на выбранную дату"
                            )
                        )
                    ]
                )
            )
        ),
        html.footer(
            {"style": footer_style},
            html.p("© Ставропольский Колледж Связи")
        )
    )


@component
def renderSchedulePage():
    return ScheduleComponent()
